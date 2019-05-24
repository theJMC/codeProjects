"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import reference as r 
#import random
#import getpass
#import appJar

class bookable():
    def __init__(self):
        pass

    def checkAvailability(self):
        pass

    def makeReservation(self):
        pass

class Hotel(bookable):
    pass

class customer():
    def __init__(self, fullName, prefName):
        self.fullName = fullName
        self.prefName = prefName
        self.records = {
            "Name": fullName,
            "Amount Spent": 0,
            "Club Points": 0,
            "Booking ID": {}
        }

def main():
    r.clear()
    print("****************************")
    print("JAM Hotel Reservation System")
    print("****************************")
    print("""    [1]: Reserve a room
    [2]: Check In
    [3]: Check Out
    [4]: Hotel Info
    [5]: Setup new Hotel
    [6]: Change Hotel
    [0]: Exit""")
    option = input("\n Please enter an option > ")
    if option == "1":
        pass
    elif option == "2":
        pass
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
    main()

if __name__ == "__main__":
    startup()