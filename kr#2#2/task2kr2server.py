#4 variant
import socket

sock = socket.socket()
sock.bind(('localhost', 50000))
sock.listen()
letters_counter = []
inp_let = (conn.recv(1024).decode('utf-8'))

def counter(let):
    alf = 'qwertyuiopasdfghjklzxcvbnm'
    for i in alf:
        if let == alf[i]:
            letters_counter[i] += 1
            print(f'{let} прислали {letters_counter[i]} раз(а)')


while True:
    letter = conn.recv(1024).decode('utf-8')
    res = counter(letter)
    conn.send(res.encode())
