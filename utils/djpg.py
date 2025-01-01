''' A set of pygame utilities '''
import pygame 

def load_sprite_sheet(lss_sheet, lss_width, lss_height):
    ''' takes a sprite sheet, width and height of the frames.
        and loads it into a list and returns it. 
    '''
    lss_frames = []
    lss_sprite_sheet = pygame.image.load(lss_sheet)
    for lss_y in range(0, lss_sprite_sheet.get_height(), lss_height):
        for lss_x in range(0, lss_sprite_sheet.get_width(), lss_width):
            lss_frame = lss_sprite_sheet.subsurface(pygame.Rect(lss_x, lss_y, lss_width, lss_height))
            lss_frames.append(lss_frame)
    return lss_frames