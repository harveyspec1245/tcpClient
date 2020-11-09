from abc import ABCMeta, abstractmethod


class Tool(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    # @abstractmethod
    # def __del__(self):
    #     pass

    @abstractmethod
    async def tcp_echo_client(self):
        pass
