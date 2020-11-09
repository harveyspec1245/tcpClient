from prometheus_client import start_http_server
from .server import Server


if __name__ == '__main__':
    print('Starting prometheus server')
    start_http_server(8000)
    server = Server('127.0.0.1', 8888)

