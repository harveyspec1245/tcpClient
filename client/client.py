import socket


class Client(object):
    def __init__(self, TCP_IP: 'str' = '127.0.0.1', TCP_PORT: 'int' = 7004, BUFFER_SIZE: 'int' = 1024) -> None:
        self.tcp_ip = TCP_IP
        self.tcp_port = TCP_PORT
        self.buffer_size = BUFFER_SIZE
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.tcp_ip, self.tcp_port))

    @staticmethod
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def send_receive_data(self, data: 'str') -> None:
        for chunk in self.chunks(data, 6):
            print('sending: ', chunk)
            self.s.send(bytes(data.encode()))
        _data_to_receive = self.s.recv(self.buffer_size)
        print('received data: ', _data_to_receive)

    def close_session(self) -> None:
        self.s.close()
