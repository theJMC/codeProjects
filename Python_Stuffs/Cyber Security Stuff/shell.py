import socket
import tqdm

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input("IP Address of server: ")


def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False


def startscan():
    portsToScan = input("Max Port to scan: ")
    with tqdm(total=str(portsToScan) + 1) as pbar:
        try:
            for x in range(1, int(portsToScan) + 1):
                if pscan(x):
                    print("Port ", x, " Is Open")
                else:
                    print("Port ", x, " Is Closed")
            pbar.update(round(portsToScan + 1 / 100, 0))
        except TypeError:
            print("Enter a Valid Number Please")
            startscan()


if __name__ == "__main__":
    startscan()
