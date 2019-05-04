"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import tube
from os import system

def main():
    system("cls")
    print("Welcome to the JMC Tube & Rail Status App")
    print("\n[1]: View All\n[2]: View Tube & DLR\n[3]: View National Rail\n[4]: Search the Network\n[9]: Sync\n[0]: Exit")
    option = input("Please select an option > ")
    if option == "1":
        print("Tube & DLR")
        print(tube_data.getTube())
        print("=================\nNational Rail")
        print(rail_data.getRail())
        input("\n\nPress enter to continue")
    elif option == "2":
        print("Tube and DLR\n" + tube_data.getTube())
        input("\n\nPress enter to continue")
    elif option == "3":
        print("National Rail\n" + rail_data.getRail())
        input("\n\nPress enter to continue")
    elif option == "4":
        pass
    elif option == "9":
        print("\nSyncing...")
        tube_data.update()
        rail_data.update()
    elif option == "0":
        raise SystemExit
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    main()

if __name__ == "__main__":
    tube_data = tube.tube()
    rail_data = tube.rail()
    main()