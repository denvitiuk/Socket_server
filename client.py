from socket import socket
import socket


class StartClient:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("localhost", 5000))

    def __del__(self):
        self.client.close()

    def rec(self, param):
        data = self.client.recv(param)
        return data

    def sendall(self, param):
        pass

    def recv(self, param):
        pass


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


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


def generate_list(range1, range2):
    list_random = []
    for i in range(int(range1), int(range2)):
        f = i + 1
        list_random.append(f)
    return list_random.sort()


def main():
    client = StartClient()

    ##########################################
    lim_one = input("Input range 1 -> ")
    lim_two = input("Input range 2 -> ")

    client.sendall(sendable_data(lim_one))
    client.sendall(sendable_data(lim_two))

    ############################################

    data = client.recv(1024)

    ready_to = data.decode()
    print("ur random numb is", ready_to)


    list_random = generate_list(lim_one, lim_two)

    ind = binarySearch(list_random, int(ready_to))
    print("num is -", ind)


if __name__ == "__main__":
    main()
