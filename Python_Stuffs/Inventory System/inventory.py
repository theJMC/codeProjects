"""
Title: Inventory System

Date: 09/02/2019

Author: James McCarthy

Notes:

Todo:

"""
import reference as ref
import random
import getpass
import os
import hashlib


# Variables

users = {0000: "Administrator", 1337: "James", 1234: ""}
adminPW = "c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec"
__user__ = ""
exit = False
stock = []

# Classes

class item:

    def __init__(self, name, location, identification):
        self.ID = identification
        self.name = name
        self.location = location

    def reserve(user):
        pass

# Functions


def login():
    while True:
        userName = input("User: ")
        if userName == "0000":
            passAttempt = getpass.getpass()
            if hashlib.sha512(passAttempt.encode()).hexdigest() == adminPW:
                break
            else:
                continue
        else: 
            break
    return int(userName)

def addStock():
    ref.clear()
    nameToAdd = input("What is the name of the item? > ")
    locationOfItem = input("Where is this item? > ")
    temp = item(nameToAdd, locationOfItem, len(stock))
    stock.append(temp)

def checkStock():
    for i in range(len(stock)):
        print(stock[i])

def deleteStock():
    pass

def reserve():
    pass

# Main

def main():
    ref.clear()
    __user__ = login()
    while exit == False:
        ref.clear()
        print("Inventory System: Welcome " + users[__user__])
        print("\n[1]: Add Stock\n[2]: Check Stock\n[3]: Remove Stock\n[5]: Reserve Stock\n[0]: Exit")
        option = input("Please select an Option: > ")
        if option == "1":
            addStock()
            print("Adding Stock")
            input("Press enter to continue")
        elif option == "2":
            checkStock()
            print("Checking Stock")
            input("Press enter to continue")
        elif option == "3":
            deleteStock()
            print("Removing Stock")
            input("Press enter to continue")
        elif option == "5":
            reserve()
            print("Reserving Stock")
            input("Press enter to continue")
        elif option == "0":
            raise SystemExit
        else:
            print("Please choose a valid option")
            continue
        




if __name__ == "__main__":
    main()