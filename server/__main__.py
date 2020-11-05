import socket
from server import Server

if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 7004
    print('listen on', host, ':', port)
    serversocket.bind((host, port))
    serversocket.listen(1)
    while 1:
        print('1\n')
        clientsocket, address = serversocket.accept()
        Server(clientsocket, address)
