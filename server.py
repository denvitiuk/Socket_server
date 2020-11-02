import socket
import random


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()


def to_get(connect_pls):
    data2 = connect_pls.recv(1024)
    f = data2.decode("utf-8").strip()
    return f


def main():

    while True:
        conn, addr = server.accept()
        print(f'{addr} has connected')
#####################################################
        f = to_get(conn)
        g = to_get(conn)

        print(f)
        print(g)

######################################################
        num = random.randint(int(f), int(g))
        conn.sendall(str(num).encode())
#######################################################


if __name__ == "__main__":
    main()
