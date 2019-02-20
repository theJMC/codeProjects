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
import csv
import time


# Variables

users = {0000: "Administrator", 1337: "James", 1234: "Mjeff"}
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

    def reserve(self, user):
        pass

# Functions


def login():
    while True:
        userName = input("User: ")
        if userName == "EXIT":
            raise SystemExit
        if len(userName) == 4:
            if userName == "0000":
                passAttempt = getpass.getpass()
                if hashlib.sha512(passAttempt.encode()).hexdigest() == adminPW:
                    break
                else:
                    continue
            else: 
                break
        else:
            print("Invalid ID")
            continue
    return int(userName)

def addStock():
    ref.clear()
    nameToAdd = input("What is the name of the item? > ")
    locationOfItem = input("Where is this item? > ")
    temp = item(nameToAdd, locationOfItem, len(stock))
    stock.append(temp)

def checkStock():
    ref.clear()
    print("Stock:\n")
    for i in range(len(stock)):
        print(stock[i].name)

def deleteStock():
    ref.clear()
    print("Please select a number to remove")
    for i in range(len(stock)):
        print("[" + str(i) + "]: " + stock[i].name)
    option = input("Select a number > ")
    try:
        del stock[int(option)]
    except IndexError:
        print("That ID is not in our database!!")
        input("Press enter to continue")
    except ValueError:
        print("Please input a number only")
        input("Press enter to continue")

def lookUp():
    itemToLookUp = input("Please enter the name or ID of an item > ")
    try: 
        itemToLookUp = int(itemToLookUp)
    except TypeError:
        itemToLookUp = str(itemToLookUp)
    if itemToLookUp == int:
        try:
            print("Name: " + stock[itemToLookUp].name)
            print("ID: " + stock[itemToLookUp].ID)
            print("Location: " + stock[itemToLookUp].location)
        except IndexError:
            print("That ID is not in our database!!")
            input("Press enter to continue")
        except ValueError:
            print("Value Error!! [HALP MEEEEE]")
            input("Press enter to continue")
    elif itemToLookUp == str:
        for i in range(len(stock)):
            if itemToLookUp in stock[i].name:
                print("Name: " + stock[itemToLookUp].name)
                print("ID: " + stock[itemToLookUp].ID)
                print("Location: " + stock[itemToLookUp].location)
            else: 
                print("Sorry that item is not in our database!!")
    else:
        print("Error in selecting Item")

def reserve():
    pass

# Main

def main():
    ref.clear()
    while exit == False:
        ref.clear()
        print("Inventory System: Welcome " + users[__user__])
        print("\n[1]: Add Stock\n[2]: Check Stock\n[3]: Remove Stock\n[4]: Look Up Item\n[5]: Reserve Stock\n[0]: Exit")
        option = input("Please select an Option: > ")
        if option == "1":
            addStock()
            input("Press enter to continue")
        elif option == "2":
            checkStock()
            input("Press enter to continue")
        elif option == "3":
            deleteStock()
            print("Removing Stock")
            input("Press enter to continue")
        elif option == "4":
            lookUp()
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
    ref.clear()
    __user__ = login()
    main()