import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()


while True:
    connect, addr = server.accept()
    print(f'{addr} has connected')
    #data = connect.recv(1024)
    num = random.randint(0,2000000)
    connect.send(repr(num).encode("utf-8"))
