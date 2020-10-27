import socket
import time
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

time_duration = float(input("ввдеіть час виділений на виконання = "))
att = 0

list_random = []
tmp_list = []

while True:
    data = client.recv(2048) # наше загадане число
    ready_to = int(data.decode("utf-8"))
    print(ready_to)

    time_start = time.time()
    while time.time() < time_start + time_duration:

        guessing = random.randint(0, 2000000)
        list_random.append(guessing)
        att += 1
        if guessing == ready_to:
            print('your number was guessed it is = ', guessing)
            print("att = ", att)
            break

    else:
        for i in list_random:
            tmp_list.append(i - ready_to)

        print("near = ", min(tmp_list) + ready_to)