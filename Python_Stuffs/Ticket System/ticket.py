"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import ref
import time
import os
import logging
import getpass
import datetime

current_station = "[Blank]"
current_zone = "[Blank]"

usernames = ["James", "root", "User"]
passwords = ["McC", "toor", "Pass"]

def clear():
    os.system('cls')

def printTickets(typeOfTicket, tube):
    clear()
    print("Ticket Options\n")
    destination = input("Destination: ")
    if tube:
        mode = "London Underground"
        zone_line = input("Destination Zone: ")
        zone_line = "Zone " + zone_line
    else:
        mode = "National Rail"
        zone_line = input("Line: ")
        zone_line = "Via " + zone_line
    
    Exit = False
    while Exit == False:
        print("Ticket Types:")
        print("[1] Adult (16+)")
        print("[2] Child (Under 16)")
        print("[3] Apprentice")
        print("[4] Student (Requires Verification)")
        print("[9] Exit")
        option = input(" >")
        if option == "1":
            ticketType = "Adult"
            Exit = True
        elif option == "2":
            ticketType = "Child"
            Exit = True
        elif option == "3":
            ticketType = "Apprentice"
            Exit = True
        elif option == "4":
            ticketType = "Student"
            Exit = True
        elif option == "9":
            tickets()
        else: 
            print("Please enter a valid option")
            clear()
    if typeOfTicket == "1":
        returnoneWay = "One Way"
    elif typeOfTicket == "2":
        returnoneWay = "Return"
    
    print("---------------------------------------")
    print(mode)
    print(returnoneWay)
    print("Destination Station: " + destination)
    print("From: " + current_station)
    print(zone_line)
    print("Type: " + ticketType)
    print("Valid on " + str(datetime.date.today()))
    print("---------------------------------------")
    option = input("Is this ok? Y/N: ")
    if option == "y" or "Y":
        print("Printing...")
        time.sleep(1)
        clear()
        print("---------------------------------------")
        print(mode)
        print(returnoneWay)
        print("Destination Station: " + destination)
        print(zone_line)
        print("Type: " + ticketType)
        print("Valid on " + str(datetime.date.today()))
        print("---------------------------------------")
        input("Press enter to continue")
        start()
    
def travelcard():
    clear()
    print("Ticket Options\n")
    Exit = False
    while Exit == False:
        try:
            Exit = True
            startZone = int(input("From Zone: "))
        except TypeError:
            print("Please input a correct value!")
            Exit = False
    Exit = False
    while Exit == False:
        try:
            Exit = True
            endZone = int(input("To Zone: "))
        except TypeError:
            print("Please input a correct value!")
            Exit = False
    if startZone == endZone and isinstance(startZone, int) and isinstance(endZone, int):
        Zones = "Zone " + str(startZone) + " Only"
    elif startZone > endZone:
        Zones = "Zone " + str(endZone) + "-" + str(startZone)
    elif startZone < endZone:
        Zones = "Zone " + str(startZone) + "-" + str(endZone)
    else:
        print("Please enter correct zones")
        travelcard()
    Exit = False
    while Exit == False:
        print("Ticket Types:")
        print("[1] Adult (16+)")
        print("[2] Child (Under 16)")
        print("[3] Apprentice")
        print("[4] Student (Requires Verification)")
        print("[9] Exit")
        option = input(" >")
        if option == "1":
            ticketType = "Adult"
            Exit = True
        elif option == "2":
            ticketType = "Child"
            Exit = True
        elif option == "3":
            ticketType = "Apprentice"
            Exit = True
        elif option == "4":
            ticketType = "Student"
            Exit = True
        elif option == "9":
            tickets()
        else: 
            print("Please enter a valid option")
            clear()
    print("")
    print("---------------------------------------")
    print("Travelcard")
    print(Zones)
    print("Issued at: " + current_station)
    print("Type: " + ticketType)
    print("Valid on " + str(datetime.date.today()))
    print("")
    print("")
    print("---------------------------------------")
    while True:
        option = input("Is this OK? Y/N: ")
        if option == "y" or "Y":
            break
        elif option == "n" or "N":
            travelcard()
        else: 
            print("Please Enter a correct option")
    print("Printing...")
    time.sleep(1)
    clear()
    print("---------------------------------------")
    print("Travelcard")
    print(Zones)
    print("Type: " + ticketType)
    print("Valid on " + str(datetime.date.today()))
    print("")
    print("")
    print("---------------------------------------")
    input("Press enter to continue")
    start()

def tickets():
    clear()
    print("Ticket Menu\n")
    print("[1] Tube Tickets")
    print("[2] National Rail Tickets")
    print("[9] Exit")
    option = input("Choose an option: ")
    if option == "1":
        clear()
        print("Tube Ticket Menu\n")
        print("[1] One Way Tickets")
        print("[2] Return Tickets")
        print("[3] Travel Cards")
        print("[9] Exit")
        option = input("Choose an option: ")
        if option == "1":
            printTickets("1", True)
        elif option == "2":
            printTickets("2", True)
        elif option == "3":
            travelcard()
        elif option == "9":
            tickets()
    elif option == "2":
        clear()
        print("Train Ticket Menu\n")
        print("[1] One Way Tickets")
        print("[2] Return Tickets")
        print("[3] Exit")
        option = input("Choose an option: ")
        if option == "1":
            printTickets("1", False)
        elif option == "2":
            printTickets("2", False)
        else: 
            print("Please input a valid option")
            time.sleep(1)
            tickets()
    elif option == "9":
        start()
    else: 
        print("Please input a valid option")
        time.sleep(1)
        tickets()


def oyster():
    clear()
    print("Oyster Menu\n")
    print("[1] Buy Oyster Card")
    print("[2] Top Up Oyster Card")
    print("[9] Exit")
    option = input("Choose an option: ")
    if option == "1":
        clear()
        print("Oyster Menu\nBuying a card\n")
        cost = input("How much do you want to put on? £")
        print("Please place the card on the vailidator...")
        input()
        print("Done!")
        time.sleep(2)
        start()
    elif option == "2":
        print("Oyster Menu\Topping Up a card\n")
        cost = input("How much do you want to put on? £")
        print("Please place the card on the vailidator...")
        input()
        print("Done!")
        time.sleep(2)
        start()
    elif option == "9":
        start()
    else:
        print("Please enter a valid option")
        time.sleep(1)
        oyster()

def config(current_station, current_zone):
    clear()
    print("Configuration\n")
    print("You are currently at " + current_station + " Station in Zone " + current_zone)
    print("\n[1] Change Station")
    print("[2] Change Zone")
    print("[9] Exit")
    option = input("Please Choose an option: ")
    if option == "1":
        print("")
        current_station = input("What Station Would You Like to change to? ")
        config(current_station, current_zone)
    elif option == "2":
        print("")
        current_zone = input("What Zone Would You Like to change to? ")
        config(current_station, current_zone)
    elif option == "9":
        start()
    else:
        print("Please enter a valid Option")
        time.sleep(2)
        config()


def start():
    clear()
    print("London Underground Tickets \n")
    print("[1] Buy Tickets")
    print("[2] Buy / Top up Oyster Card")
    print("[3] Options")
    print("[9] Exit")
    option = input("Choose an option: ")
    if option == "1":
        tickets()
    elif option == "2":
        oyster()
    elif option == "3":
        config(current_station, current_zone)
    elif option == "9":
        exit()
    else:
        print("Please enter a valid option")
        time.sleep(1)
        start()

start()