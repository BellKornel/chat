import socket
from threading import Thread


def send():
    while True:
        msg = input('\nMe > ')
        cli_sock.send(bytes(msg, 'utf-8'))


def receive():
    while True:
        sen_name = cli_sock.recv(1024).decode('utf-8')
        data = cli_sock.recv(1024).decode('utf-8')

        print('\n' + str(sen_name) + ' > ' + str(data))


if __name__ == '__main__':
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 7777
    cli_sock.connect((host, port))
    print('Connected to host...')
    uname = input('Enter your name: ')
    cli_sock.send(bytes(uname, 'utf-8'))

    ts = Thread(target=send)
    ts.start()

    tr = Thread(target=receive)
    tr.start()
