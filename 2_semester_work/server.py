import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 4548))
server.listen()
users = []
phrases = ['its your turn', 'please, wait', 'please choose the second card', 'yeah, you are the winner, great', 'sorry, you are loser', 'do you wanna restart the game?']

def users_amount():
    while True:
        user, addr = server.accept()
        users.append(user)
        if len(users) < 3:
            continue

# def players_sending_messages(first_player, second_player):
