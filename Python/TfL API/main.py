"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

TODO Add Routes

"""
import tube
from os import system

def status():
    system("cls")
    print("Welcome to the JMC Tube & Rail App")
    print("\n[1]: View All \n[2]: View Tube & DLR\n[3]: View National Rail\n[9]: Sync\n[0]: Back")
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
    elif option == "9":
        print("\nSyncing...")
        tube_data.update()
        rail_data.update()
    elif option == "0":
        main()
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    status()

def station():
    system("cls")
    print("Welcome to the JMC Tube & Rail App")
    print("\n[1]: View All Stations \n[2]: View Stations on a line\n[3]: Convert ID to Name\n[4]: Convert Name to ID\n[9]: Sync\n[0]: Back")
    option = input("Please select an option > ")
    if option == "1":
        for item in tube_data.getAllStations(False):
            print(item)
        input("\n\nPress enter to continue")
    elif option == "2":
        system("cls")
        lines = tube_data.getLines(False)
        lines_id = tube_data.getLines(True)
        print("Welcome to the JMC Tube & Rail App")
        for i in range(len(lines)):
            print("[" + str(i+1) + "]: " + lines[i]) 
        option = input("Please select an option > ")
        system("cls")
        try:
            for item in tube_data.getStationsOnLine(lines_id[int(option)-1]):
                print(item)
        except IndexError:
            print("Thats not an option!")
        input("\n\nPress enter to continue")
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "9":
        print("\nSyncing...")
        tube_data.update()
        rail_data.update()
    elif option == "0":
        main()
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    station()

def fares():
    system("cls")
    print("Welcome to the JMC Tube & Rail App")
    print("\n[1]: View All Fares \n[2]: Select Route\n[9]: Sync\n[0]: Back")
    option = input("Please select an option > ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "9":
        print("\nSyncing...")
        tube_data.update()
        rail_data.update()
    elif option == "0":
        main()
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    fares()

def lines():
    system("cls")
    print("Welcome to the JMC Tube & Rail App")
    print("\n[1]: View All Lines \n[2]: View Routes on a line\n[9]: Sync\n[0]: Back")
    option = input("Please select an option > ")
    if option == "1":
        system("cls")
        for item in tube_data.getLines(False):
            print(item)
        input("\n\nPress enter to continue")
    elif option == "2":
        system("cls")
        lines_list = tube_data.getLines(False)
        lines_id = tube_data.getLines(True)
        print("Welcome to the JMC Tube & Rail App")
        for i in range(len(lines_list)):
            print("[" + str(i+1) + "]: " + lines_list[i]) 
        option = input("Please select an option > ")
        system("cls")
        try:
            for item in tube_data.getRoutesOnLine(lines_id[int(option)-1]):
                print(item)
        except IndexError:
            print("Thats not an option!")
        input("\n\nPress enter to continue")
        # input("\n\nPress enter to continue")
    elif option == "9":
        print("\nSyncing...")
        tube_data.update()
        rail_data.update()
    elif option == "0":
        main()
    else:
        print("Thats not an option!")
        input("Press enter to continue... ")
    lines()


def main():
    system("cls")
    print("Welcome to the JMC Tube & Rail App")
    print("\n[1]: View Statuses\n[2]: View Stations\n[3]: View Fares\n[4]: View Lines\n[9]: Sync\n[0]: Exit")
    option = input("Please select an option > ")
    if option == "1":
        status()
    elif option == "2":
        station()
    elif option == "3":
        fares()
    elif option == "4":
        lines()
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