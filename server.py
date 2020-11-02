from socket import socket
import socket
import random


class Start:

        def __init__(self):

            self.connect = None
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(("localhost", 5000))
            self.server.listen()
            self.num = None

        def connection(self):
            self.connect, addr = self.server.accept()
            print(f'{addr} has connected')

        def send_random(self, range1, range2):
            # data = connect.recv(1024)
            self.num = random.randint(range1, range2)
            return self.num

        def rec(self, param):
            data = self.server.recv(param)
            return data

        def __del__(self):
            self.server.close()

        def accept(self):
            conn, addr = self.server.accept()
            return conn, addr


def main():

    server = Start()

    while True:
        conn, addr = server.accept()
        print(f'{addr} has connected')
        #####################################################
        data = conn.recv(1024)
        data2 = conn.recv(1024)
        f = data.decode("utf-8").strip()
        g = data2.decode("utf-8").strip()

        ######################################################
        num = server.send_random(int(f), int(g))
        conn.sendall(str(num).encode())
    #######################################################


if __name__ == "__main__":
    main()
