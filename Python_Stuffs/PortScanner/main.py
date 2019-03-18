"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
#import reference
#import random
#import getpass
#import appJar
import socket
import sys

option = sys.argv[1]
try:
    target_ip = sys.argv[2]
except IndexError:
    pass
try:
    target_port = sys.argv[3]
except IndexError:
    pass
try:
    end_range_port = sys.argv[4]
except IndexError:
    pass

helpMessage = ("""JAM PORT SCANNER 1.0
    portScan.py [option] [target ip] [target port] [End Range Port]
Options:
    -h : Help, Shows this menu
    -a : Scam all ports (no target port needed)
    -s : Scan Selected Port 
    -sR : Scan Selected Port Range
""")

def scanPort(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, int(port)))
    if result == 0:
        print("Port {}:  Open".format(port))
    sock.close()

def main():
    if option == "-h":
        print(helpMessage)
    elif option == "-a":
        for i in range(1,500):
            scanPort(target_ip, i)
    elif option == "-s":
        scanPort(target_ip, target_port)
    elif option == "-sR":
        for i in range(int(target_port), int(end_range_port)):
            scanPort(target_ip, int(i))
    else:
        print("Option Unavailable")
    
if __name__ == "__main__":
    main()