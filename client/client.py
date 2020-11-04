import socket
import sys

# TCP_IP = '127.0.0.1'
# TCP_PORT = 7004
# BUFFER_SIZE = 20


class Client(object):
    def __init__(self, TCP_IP:'str' = '127.0.0.1', TCP_PORT:'int' = 7004, BUFFER_SIZE:'int' = 20) -> None:
        self.tcp_ip = TCP_IP
        self.tcp_port = TCP_PORT
        self.buffer_size = BUFFER_SIZE
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.tcp_ip, self.tcp_port))

    def send_data(self):
        _data_list = sys.argv[1:]
        _data = bytes(_data_list[0].encode())
        self.s.send(_data)
        data = self.s.recv(self.buffer_size)
        print('received data: ', data)

    def close_session(self):
        self.s.close()
