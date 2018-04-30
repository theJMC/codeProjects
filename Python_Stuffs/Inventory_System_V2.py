import time
import os
import os.path
import datetime
import csv
import progressbar
import pandas as pd

# class Stock:
#     def __init__(self, name, out, outBy, takenOut, dueIn):
#         self.name = name
#         self.out = out
#         self.outBy = outBy
#         self.takenOut = takenOut
#         self.dueIn = dueIn

tday = datetime.date.today()

inventory = []

bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

def reload_variables():
    inventory.clear()
    print("Reloading Stock")
    try:
        with open ('stock.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            x=0
            for line in csv_reader:
                inventory.insert(x, line)
                bar.update(x)
                time.sleep(0.25)
                # next(csv_reader)
                x=x+1
    except Exception:
        f = open("stock.csv", "w+")
        f.write("")
        f.close
        reload_variables()
    
            
# inventory = [Stock("iPad 2017", "No", "N/A", "N/A", "N/A"), Stock("iPhone X", "No", "N/A", "N/A", "N/A")]

def checkIn():
    print("Checking In Stock...")
    selection = input("ID of Item ")
    try:
        print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("ID", "Name:", "Out:", "By Who:", "Taken Out", "Due Date:"))
        print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("[" + str(selection) + "]", inventory[int(selection)][1], inventory[int(selection)][2], inventory[int(selection)][3], inventory[int(selection)][4], inventory[int(selection)][5]))
        confirm = input("Are you sure you want to return the " + inventory[int(selection)][1] + "? Y/n ")
        if confirm == "y" or "Y":
            inventory[int(selection)][2] = "No"
            inventory[int(selection)][3] = " "
            inventory[int(selection)][4] = " "
            inventory[int(selection)][5] = " " 
            df = pd.read_csv("stock.csv")
            df.iat[int(selection), 2] = "No"
            df.iat[int(selection), 3] = " "
            df.iat[int(selection), 4] = " "
            df.iat[int(selection), 5] = " "
            df.to_csv("stock.csv", index=False)
        else:
            print("Request Declined")
        input("Press Enter to continue")
        print("Done!\n\n")
    except ValueError:
        print("Please Enter a number")
        input("Press Enter to Continue")
        os.system('cls')
        checkIn()
    if __name__ == '__main__':
        start()

def checkOut():
    print("Checking Out Stock...")
    selection = input("ID of item: ")
    print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("ID", "Name:", "Out:", "By Who:", "Taken Out", "Due Date:"))
    print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("[" + inventory[int(selection)][0] + "]", inventory[int(selection)][1], inventory[int(selection)][2], inventory[int(selection)][3], inventory[int(selection)][4], inventory[int(selection)][5]))
    confirm = input("Are you sure you want to take out the " + inventory[int(selection)][1] + "? Y/n")
    if confirm == "y" or "Y":
        time = input("How long would you like the item? (Weeks) ")
        username = input("What name would you like to register this transaction to? ")
        inventory[int(selection)][2] = "Yes"
        inventory[int(selection)][3] = username
        inventory[int(selection)][4] = tday
        inventory[int(selection)][5] = str(tday + datetime.timedelta(weeks=int(time)))
        df = pd.read_csv("stock.csv")
        df.iat[int(selection), 1] = "Yes"
        df.iat[int(selection), 2] = username
        df.iat[int(selection), 3] = tday
        df.iat[int(selection), 4] = tday + datetime.timedelta(weeks=int(time))
        # df.set_value(int(selection), "dueIn", str(tday + datetime.timedelta(weeks=int(time))))
        df.to_csv("stock.csv", index=False)
    else:
        print("Request Declined")
    input("Press Enter to continue")
    print("Done!\n\n")
    if __name__ == '__main__':
        start()

def checkInventory():
    print("Checking Inventory Stock...")
    print('{:<12}  {:<15}  {:<12}  {:<12}  {:<20}'.format("ID", "Name:", "Out:", "By Who:", "Due Date:"))
    for i in range(0,len(inventory)):
    # print(inventory)
        print('{:<12}  {:<15}  {:<12}  {:<12}  {:<20}'.format("[" + str(inventory[int(i)][0])+ "]", inventory[int(i)][1], inventory[int(i)][2], inventory[int(i)][3], inventory[int(i)][5]))
    print("\n\n")
    input("Press Enter to Continue")
    if __name__ == '__main__':
        start()

def addStock():
    print("Adding Stock...")
    nameOfItem = input("Name: ")
    data = [len(inventory), nameOfItem, "No", " ", " ", " "]
    inventory.append(data)
    # print(inventory)
    with open ('stock.csv', 'a') as csv_file_writer:
        csv_writer = csv.writer(csv_file_writer)
        csv_writer.writerow(data)
    print("Done!\n\n")
    input("Press Enter to continue")
    if __name__ == '__main__':
        start()

def removeStock():
    print("Removing Stock...")
    selection = input("Item ID: ")
    print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("ID", "Name:", "Out:", "By Who:", "Taken Out", "Due Date:"))
    print('{:<12}  {:<15}  {:<12}  {:<12}  {:<12}  {:<20}'.format("[" + str(selection) + "]", inventory[int(selection)][2], inventory[int(selection)][3], inventory[int(selection)][4], inventory[int(selection)][5], inventory[int(selection)][6]))
    confirm = input("Are you sure you want to remove the " + inventory[int(selection)].name + " from the system? Y/n: ")
    if confirm == "y" or "Y":
        inventory.pop(int(selection))
    else:
        print("Request Declined")
    print("Done!\n\n")
    input("Press Enter to continue")
    if __name__ == '__main__':
        start()

def kill():
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    print("Hello and welcome to the JAM Product Inventory System\nPlease Select an option:")
    print("""
[1] Check In
[2] Check Out
[3] Check Inventory
[4] Add Stock
[5] Remove Stock
[6] Reload Stock
[7] Exit
    """)
    option = input("Option: ")
    if option == "1":
        checkIn()
    elif option == "2":
        checkOut()
    elif option == "3":
        checkInventory()
    elif option == "4":
        addStock()
    elif option == "5":
        removeStock()
    elif option == "6":
        reload_variables()
        start()
    elif option == "7":
        exit()
    else:
        print("Error 504: Incorrect Selection")
        start()

if __name__ == '__main__':
    reload_variables()
    start()