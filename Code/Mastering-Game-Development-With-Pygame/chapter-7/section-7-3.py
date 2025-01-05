''' section 7.3'''
import sys
import pygame
import random
import heapq
import socket
import threading

sys.path.append("../../utils")
import rgb
import djpg


def handle_client(hc_client_socket):
    ''' function to handle the client'''
    while True:
        hc_request = hc_client_socket.recv(1024)
        if not hc_request:
            break
        print(f"Received: {hc_request.decode()}")
        hc_client_socket.send(b"ACK!")


def run_server():
    ''' function to run the server '''
    rs_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rs_server.bind(("0.0.0.0", 8888))
    rs_server.listen(5)
    print("Server Listening on port 8888")
    while True:
        rs_client_socket, rs_addr = rs_server.accept()
        print(f"Accepted connection from {rs_addr[0]}:{rs_addr[1]}")
        rs_client_handler = threading.Thread(target=handle_client, args=(rs_client_socket,))
        rs_client_handler.start()


def run_client():
    ''' function to run the client '''
    rc_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rc_client.connect(("127.0.0.1", 8888))
    while True:
        rc_message = input("Enter a message : ")
        rc_client.send(rc_message.encode())
        rc_response = rc_client.recv(1024)
        print(f"Received from server {rc_response.decode()}")


def main():
    ''' Main Function'''
    # initialise pygame
    server_thread = threading.Thread(target=run_server)
    client_thread = threading.Thread(target=run_client)
    server_thread.start()
    client_thread.start()


if __name__ == "__main__":
    main()
