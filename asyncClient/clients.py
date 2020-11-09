from .client import Client


class Clients(object):
    def __init__(self, instance, message):
        self.instance = instance
        self.message = message
        self.client_instance_creator()

    def client_instance_creator(self):
        for instance in range(self.instance):
            Client(message=self.message)
            self.message += str('aaaaaaaaaaaaaaaaaaaaaa')


