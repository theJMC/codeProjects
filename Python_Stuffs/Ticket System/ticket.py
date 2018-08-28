import time
import os
import logging

current_station = ""
current_zone = ""

def clear():
    os.system('cls')

def printTickets(typeOfTicket):
    clear()
    print("Ticket Options\n")
    destination = input("Destination: ")
    dest_zone = input("Destination Zone: ")
    Exit = False
    while Exit == False:
        print("Ticket Types:")
        print("[1] Adult (16+)")
        print("[2] Child (Under 16)")
        print("[3] Apprentice")
        print("[4] Student (Requires Verification)")
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
        else: 
            print("Please enter a valid option")
            clear()
    if typeOfTicket == "1":
        returnoneWay = "One Way"
    elif typeOfTicket == "2":
        returnoneWay = "Return"
    print("---------------------------------------")
    print(returnoneWay)
    print("Destination Station: " + destination)
    print("Destination Zone: " + dest_zone)
    print("Type: " + ticketType)
    print("---------------------------------------")
    option = input("Is this ok? Y/N: ")
    if option == "y" or "Y":
        print("Printing...")
        time.sleep(1)
        clear()
        print("---------------------------------------")
        print(returnoneWay)
        print("Destination Station: " + destination)
        print("Destination Zone: " + dest_zone)
        print("Type: " + ticketType)
        print("---------------------------------------")
        input("Press enter to continue")
        start()
    

def tickets():
    clear()
    print("Ticket Menu\n")
    print("[1] Tube Tickets")
    print("[2] National Rail Tickets")
    print("[3] Exit")
    option = input("Choose an option: ")
    if option == "1":
        clear()
        print("Tube Ticket Menu\n")
        print("[1] One Way Tickets")
        print("[2] Return Tickets")
        print("[3] Travel Cards")
        print("[4] Exit")
        option = input("Choose an option: ")
        if option == "1":
            printTickets("1")
        elif option == "2":
            printTickets("2")
    elif option == "2":
        print("Train Tickets")
        time.sleep(1)
    elif option == "3":
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
    print("[3] Exit")
    option = input("Choose an option: ")
    if option == "1":
        clear()
        print("Oyster Menu\nBuying a card\n")
        cost = input("How much do you want to put on? £")
        print("Please place the card on the vailidator...")
        os.system("pause")
        print("Done!")
        time.sleep(2)
        start
    elif option == "2":
        print("Topping up Oyster Card")
        time.sleep(2)
        start()
    elif option == "3":
        start()
    else:
        print("Please enter a valid option")
        time.sleep(1)
        oyster()

def start():
    clear()
    print("London Underground Tickets \n")
    print("[1] Buy Tickets")
    print("[2] Buy / Top up Oyster Card")
    print("[3] Exit")
    option = input("Choose an option: ")
    if option == "1":
        tickets()
    elif option == "2":
        oyster()
    elif option == "3":
        print("Please enter a valid option")
        time.sleep(1)
        exit()

start()