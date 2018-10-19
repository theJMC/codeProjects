"""try:

except Error as e:
Title: Reference File

Date: 07/10/2018

Author: James McCarthy

Notes: Its My Python Reference Package, full of lots of reusable functions
        Colour File (Colour)
        Login Script (Login)


Todo:

"""
#import random
#import getpass
#import appJar

class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def login(usernames, passwords):
    usernames.append("admin")
    passwords.append("admin")


