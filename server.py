import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 500))
    server.listen()
    while True:
        client, addr = server.accept()
        request = client.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)

        client.sendall("Hello world".encode())
        client.close()


if __name__ == "__main__":
    main()
