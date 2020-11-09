import asyncio
from prometheus_client import Summary


class Server(object):
    REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.coro = asyncio.start_server(self.handle_echo, self.ip, self.port, loop=self.loop)
        self.server = self.loop.run_until_complete(self.coro)
        self.run_server()

    def run_server(self):
        print('Serving on {}'.format(self.server.sockets[0].getsockname()))
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass

    def stop_server(self):
        print('aaaa')
        self.server.close()
        self.loop.run_until_complete(self.server.wait_closed())
        self.loop.close()
        print('bbbb')

    @REQUEST_TIME.time()
    async def handle_echo(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))

        print("Send: %r" % message)
        writer.write(data)
        await writer.drain()

        print("Close the client socket")
        writer.close()





