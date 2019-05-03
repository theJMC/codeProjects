"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
from tube import tubeStatus, natrailStatus
from os import system

def main():
    system("cls")
    print("Welcome to the JMC Tube & Rail Status App")
    print("\n[1]: View All\n[2]: View Tube & DLR\n[3]: View National Rail\n[4]: Search the Network\n[0]: Exit")
    option = input("Please select an option > ")
    if option == "1":
        print("Tube & DLR")
        print(tubeStatus(True, True))
        print("=================\nNational Rail")
        print(natrailStatus())
        input("\n\nPress enter to continue")
    elif option == "2":
        print("Tube and DLR\n" + tubeStatus(True, True))
        input("\n\nPress enter to continue")
    elif option == "3":
        print("National Rail\n" + natrailStatus())
        input("\n\nPress enter to continue")
    elif option == "4":
        pass
    elif option == "0":
        raise SystemExit
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    main()

if __name__ == "__main__":
    main()