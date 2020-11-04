import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7004
print('listen on', host, ':', port)
serversocket.bind((host, port))


class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'Oi you sent something to me')


serversocket.listen(5)
while 1:
    clientsocket, address = serversocket.accept()
    Client(clientsocket, address)
