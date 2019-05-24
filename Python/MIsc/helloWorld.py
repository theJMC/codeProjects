import getpass
import time


def Login():
    uname = input("Username: ")
    pword = getpass.getpass()

    if uname == "root":
        if pword == "toor":
            print("Logged in successfully")
        else:
            print("Password incorrect")
            exit()
    else:
        print("User does not exist!")
        exit()


