"""
Title:

Date: 00/00/2019

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
    def __init__(self, MaxRoomNum, location):
        self.MaxRoomNum = MaxRoomNum
        self.location = location
        self.roomsReserved = []

class roomReservation():

    def __init__(self, num, name, teir, floor):
        self.roomNum = num
        self.reserveeName = name
        self.roomTeir = teir
        self.floor = floor
    



def main():
    pass

if __name__ == "__main__":
    main()