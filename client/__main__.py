from .client import Client

if __name__ == '__main__':
    new_client = Client()
    new_client.send_data()
    new_client.close_session()
