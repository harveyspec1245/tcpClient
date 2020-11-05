from threading import *
from socket import error as SocketError
import errno


class Server(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('2\n')
            try:
                _received_data = self.sock.recv(1024).decode()
                print('Client sent:', _received_data)
                self.sock.send(b'you sent something to me')
                #self.sock.close()
                break
            except SocketError as e:
                if e.errno != errno.ECONNRESET:
                    raise
                else:
                    pass
