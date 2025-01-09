''' tic tac toe '''
import sys
import pygame

sys.path.append("../../utils")
import rgb


def initialize_game_values():
    ''' initialise the game '''
    global board
    global game_over
    global X_placed
    global O_placed
    global winner
    global clock
    board = []
    game_over = False
    X_placed = False
    O_placed = False
    winner = ""
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    clock = pygame.time.Clock()


def draw_game_over_screen():
    ''' game over screen '''
    print("Game Over")
    game_window.fill(rgb.WHITE)
    if winner == 'X':
        text = font.render('X wins', True, rgb.BLACK)
    elif winner == 'O':
        text = font.render('O wins', True, rgb.BLACK)
    else:
        text = font.render('Draw!', True, rgb.BLACK)

    playAgainText = smallfont.render("Play Again (y/n)", True, rgb.BLACK)

    game_window.blit(text, (window_width/2 - 200, window_height/2 - 100))
    game_window.blit(playAgainText, (window_width/2 - 200, window_height/2 + 50))


def check_for_quit_event():
    ''' checking if the we are quitting the game '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                initialize_game_values()
                game_window.fill(rgb.WHITE)
                return True
            elif event.key == pygame.K_n:
                pygame.quit()
                quit()


def handle_mouse_down_for_x():
    ''' mouse event '''
    (col, row) = pygame.mouse.get_pos()
    row = int(row / grid_height)
    col = int(row / grid_width)
    board[row][col] = 'X'


def run_event_processing():
    ''' event processing check '''
    global X_placed
    global game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_down_for_x()
            X_placed = True


def draw_game_board_square(dgbs_row, dgbs_col):
    ''' draw square '''
    dgbs_rect = pygame.Rect(dgbs_col * grid_width,
                            dgbs_row * grid_height,
                            grid_width,
                            grid_height)
    pygame.draw.rect(game_window, rgb.BLACK, dgbs_rect, 3)


def draw_tic_tac_toe_letter(dtttl_row, dtttl_col, dtttl_letter):
    ''' draw letter '''
    dtttl_letter_piece = font.render(dtttl_letter, True, rgb.BLACK)
    game_window.blit(dtttl_letter_piece,
                     (dtttl_row * grid_width + grid_width/4,
                      dtttl_col * grid_height + grid_height/4))


def draw_the_board():
    ''' draw the game board'''
    for row in range(grid_size):
        for col in range(grid_size):
            draw_game_board_square(row, col)
            if (board[row][col] == 'X'):
                draw_tic_tac_toe_letter(row, col, 'X')
            if (board[row][col] == 'O'):
                draw_tic_tac_toe_letter(row, col, 'O')


def run_algorithm_to_place_O():
    ''' place an O '''
    for rowo in range(grid_size):
        for colo in range(grid_size):
            if (board[rowo][colo] == 0):
                board[rowo][colo] = 'O'
                return True
    return False


def check_if_anyone_won():
    '''check for a winner'''
    global winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            winner = board[row][0]
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            winner = board[0][col]
            return True

    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
        return True

    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
        return True

    if board[0][2] == board[1][1] == board[2][0] != 0:
        winner = board[0][2]
        return True

    return False


def check_if_board_is_full():
    ''' check for a full board'''
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True


def check_if_draw():
    ''' check for a draw '''
    return not (check_if_anyone_won()) and check_if_board_is_full()


def is_winning_move(player, row, col):
    ''' is this a winning move '''
    n = len(board)
    if all(board[row][j] == player for j in range(n)):
        return True
    if all(board[i][col] == player for i in range(n)):
        return True
    if row == col and all (board[i][i] == player for i in range(n)):
        return True
    if row + col  == n - 1 and all(board[i][n - i - 1] == player for i in range(n)):
        return True 
    return False


def get_empty_positions():
    ''' return the emprty slots'''
    empty_positions = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                empty_positions.append((i, j))
    return empty_positions


def run_better_algorithim_to_place_O():
    ''' better O player AI '''
    grid_size = len(board)
    empty_positions = get_empty_positions()
    num_moves = sum(1 for row in board for cell in row if cell != 0)
    if num_moves == 1:
        center = grid_size // 2
        if board[center][center] == 0:
            board[center][center] = 'O'
            return True
        else:
            for row,col in [(0, 0),
                            (0, grid_size - 1),
                            (grid_size - 1, grid_size -1 )]:
                if board[row][col] == 0:
                    board[row][col] = 'O'
                    return True
    for row,col in empty_positions:
        board[row][col] = "O"
        if is_winning_move("O", row, col):
            return True
        board[row][col] = 0

    for row,col in empty_positions:
        board[row][col] = "X"
        if is_winning_move("X", row, col):
            board[row][col] = "O"
            return True
        board[row][col] = 0

    if board[0][0] == 'O' or board[0][grid_size -1] == 'O' or board[grid_size -1][0] == 'O' or board[grid_size -1][grid_size -1] == 'O':
        for row, col in [(0,0), (0, grid_size -1), (grid_size -1, 0), (grid_size -1 , grid_size -1)]:
            if board[row][col] == 0:
                board[row][col] = "O"
                return True
    for row,col in empty_positions:
        if row not in [0, grid_size -1] and col not in [0, grid_size -1]:
            board[row][col] = "O"
            return True
                
    for row,col in empty_positions:
        board[row][col] = "O"
        return True

    return False

                
def main():
    ''' Main Function'''
    global game_window
    global window_width
    global window_height
    global font
    global smallfont
    global grid_size
    global grid_width
    global grid_height
    global board
    global clock

    # initialise pygame
    pygame.init()

    # create a game window
    window_width = 800
    window_height = 600
    game_window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tic Tac Toe")

    font = pygame.font.Font(None, 150)
    smallfont = pygame.font.Font(None, 50)

    # set the game running flag to true
    running = True
    game_over = False
    X_placed = False
    clock = pygame.time.Clock()
    grid_size = 3
    grid_width = window_width / grid_size
    grid_height = window_height / grid_size
    initialize_game_values()

    # run the game loop
    while running:
        if game_over:
            pygame.display.flip()
            pygame.time.delay(1000)
            draw_game_over_screen()
            check_for_quit_event()
        else:
            game_window.fill(rgb.WHITE)
            run_event_processing()
            draw_the_board()
            pygame.display.flip()

        if game_over:
            continue

        if X_placed:
            pygame.time.delay(500)
            O_placed = run_algorithm_to_place_O()
            game_over = check_if_anyone_won()
            draw_the_board()
            X_placed = False
        pygame.display.flip
        clock.tick(60)


if __name__ == "__main__":
    main()
