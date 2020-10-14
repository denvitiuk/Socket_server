"""
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
"""
import random

# загадане число від 0 до 2000 (нехай 59) є час за який random ьфє проходити по списку і в по закінченню часу видать або
# вгадане число або саме найближче до нього та кількість ітерацій рандомом

import time
import random
from tqdm import tqdm

random.seed()

time_duration = float(input("ввдеіть час виділений на виконання = "))
att = 0
starTime = time.time()

time_start = time.time()
list_random = []
tmp_list = []
while time.time() < time_start + time_duration:

    guessing = random.randint(0, 2000000)
    list_random.append(guessing)
    att += 1
    if guessing == 53:
        print('your number was guessed it is = ', guessing)
        print("att = ", att)
        break
else:
    for i in list_random:
        tmp_list.append(i - 53)

    print("near = ", min(tmp_list) + 53)

task_time = time.time() - starTime
print(task_time)
