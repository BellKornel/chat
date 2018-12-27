import socket
from threading import Thread


def accept_client():
    while True:
        cli_sock, cli_add = sock.accept()
        uname = cli_sock.recv(1024).decode('utf-8')
        connection_list.append((uname, cli_sock))
        print('%s is now connected!' % uname)
        bu = Thread(target=broadcast_user, args=[uname, cli_sock])
        bu.start()


def broadcast_user(uname, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                print('{0} spoke'.format(uname))
                b_usr(cli_sock, uname, data)
        except Exception as x:
            print(x.args)
            break


def b_usr(cs_sock, sen_name, msg):
    for client in connection_list:
        if client[1] != cs_sock:
            client[1].send(bytes(sen_name, 'utf-8'))
            client[1].send(msg)


if __name__ == '__main__':
    connection_list = []

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 7777

    sock.bind((host, port))

    sock.listen(32)

    print('Chat successfully started!')

    ac = Thread(target=accept_client)
    ac.start()
