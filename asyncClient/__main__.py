from asyncClient import Clients
import sys
import getopt

if __name__ == '__main__':
    _clients = 2
    _data = 'Hello'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:c:", ["data=", "clients="])
    except getopt.GetoptError as e:
        print(e)
        print('Usage: python -m client -d <data_to_send> -c <num of clients>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: python -m client -d <data_to_send> -c <num of clients>')
            sys.exit()
        elif opt in ("-d", "--data"):
            _data = arg
        elif opt in ("-c", "--clients"):
            _clients = int(arg)

    Clients(_clients, _data)
