#4 variant
import socket

sock = socket.socket()
sock.bind(('localhost', 50000))
conn, add = sock.accept()


while True:
    letter = input('Введите букву')
    sock.send(letter.encode())
    res = (sock.recv(1024)).decode()
    print(res)
