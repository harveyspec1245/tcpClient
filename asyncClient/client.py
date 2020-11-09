import asyncio
from .tool import Tool


class Client(Tool):
    def __init__(self, message):
        self._ip = '127.0.0.1'
        self._port = 8888
        self.message = message
        self._loop = asyncio.get_event_loop()
        self._loop.run_until_complete(self.tcp_echo_client())

    # def __del__(self) -> None:
    #     self._loop.close()

    async def tcp_echo_client(self) -> object:
        _reader, _writer = await asyncio.open_connection(self._ip, self._port, loop=self._loop)

        print('Send: %r' % self.message)
        _writer.write(self.message.encode())

        _data = await _reader.read(100)
        print('Received: %r' % _data.decode())

        print('Client close the socket')
        _writer.close()




