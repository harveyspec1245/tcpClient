from client import Client
import sys
import getopt

if __name__ == '__main__':
    new_client = Client()
    _close_session = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:c", ["data=", "close="])
    except getopt.GetoptError as e:
        print(e)
        print('Usage: python -m client -d <data_to_send> -c <close session>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: python -m client -d <data_to_send> -c <close session>')
            sys.exit()
        elif opt in ("-d", "--data"):
            _data_to_send = arg
            new_client.send_receive_data(_data_to_send)
        elif opt in ("-c", "--close"):
            _close_session = arg
            new_client.close_session()




