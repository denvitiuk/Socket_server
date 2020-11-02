import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


##########################################
range1 = input("Input range 1 -> ")
range2 = input("Input range 2 -> ")

client.sendall(sendable_data(range1))
client.sendall(sendable_data(range2))

############################################

data = client.recv(1024)

ready_to = data.decode()
print("ur random numb is", ready_to)

list_random = []
for i in range(int(range1), int(range2)):
    f = i + 1
    list_random.append(f)
list_random.sort()


def binarySearch(data, val):
    lo, hi = 0, len(data) - 1
    best_ind = lo
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if data[mid] < val:
            lo = mid + 1
        elif data[mid] > val:
            hi = mid - 1
        else:
            best_ind = mid
            break
        # check if data[mid] is closer to val than data[best_ind]
        if abs(data[mid] - val) < abs(data[best_ind] - val):
            best_ind = mid
    return best_ind


ind = binarySearch(list_random, int(ready_to))
print("num is -", ind + 1)
