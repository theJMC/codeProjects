"""
Title:

Date: 01/03/2019

Author: James McCarthy

Notes:

Todo:

"""
import reference
#import random
#import getpass
#import appJar

###CLASSES###

class Hotel():
    #To allow multiple Hotels to be monitored in one instance
    def __init__(self, name, MaxRoomNum, location):
        self.name = name
        self.MaxRoomNum = MaxRoomNum
        self.location = location
        self.roomsReserved = []

class roomReservation():

    def __init__(self, num, name, teir, floor):
        self.roomNum = num
        self.reserveeName = name
        self.roomTeir = teir
        self.floor = floor
    

def setUpHotel(Name, MaxRoomNum, Location):
    hotels.append(Hotel(Name, MaxRoomNum, Location))

def reserve():
    name = input("What is the name of the client? > ")
    print("What level room are you booking?:\n[1]: Standard\n[2]: Premier\n[3]: Buissness")
    teir = input("> ")
    roomNum = input("What number room is it? > ")
    floor = input("What floor is the room on? > ")
    reservations.append(roomReservation(roomNum, name, teir, floor))

def main():
    reference.clear()
    print("****************************")
    print("JAM Hotel Reservation System")
    print("****************************")
    print("Hotel: {}\n".format(hotels[active].name))
    print("""    [1]: Reserve a room
    [2]: Check In
    [3]: Check Out
    [4]: Hotel Info
    [5]: Setup new Hotel
    [6]: Change Hotel
    [0]: Exit""")
    option = input("\n Please enter an option > ")
    if option == "1":
        reserve()
        main()
    elif option == "2":
        for i in range(len(reservations)):
            print(reservations[i].roomNum)
            print(reservations[i].reserveeName)
            print(reservations[i].roomTeir)
            print(reservations[i].floor)
        main()
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "0":
        raise SystemExit
    else:
        print("Please enter a valid option")
        input("Press enter to continue...")
        main()

def startup():
    reference.clear()
    hotelName = input("Whats the name of you hotel? > ")
    hotelNums = input("How many rooms are in the Hotel? > ")
    hotelLocation = input("Where is the hotel? > ")
    setUpHotel(hotelName, hotelNums, hotelLocation)
    main()

if __name__ == "__main__":
    hotels = []
    reservations = []
    active = 0
    startup()