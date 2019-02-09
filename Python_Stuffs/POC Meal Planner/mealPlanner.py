"""
Title: Meal Planner

Date: 01/02/2019

Author: James McCarthy

Notes:

Todo:

"""
import reference
import time

meals = [["Southern Baked Chicken"], ["Spag Bol"], ["Chicken Tikka Nuggets"], ["BBQ Chicken"], ["Tacos"], ["Tikka Cod"]]


def main():
    reference.clear()
    print('''
McCarthy Meal Planner - 
[1] - Start Meal Plan
[2] - See Index
[3] - Search Recipes 
[0] - Exit
          ''')
    option = input("What option do you want to do? > ")
    if option == "1":
        print("Starting Meal Plan")
        time.sleep(2)

        main()
    elif option == "2":
        for i in range(len(meals)):
            print(meals[i][0])
        main()
    elif option == "3":
        print("Searching Recipes")
        main()
    elif option == "0":
        exit()


if __name__ == "__main__":
    main()
