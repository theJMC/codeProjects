"""
# Creates an SQL connection to the employee.db file
conn = sqlite3.connect('employee.db')
# Creates a cursor for the created database
c = conn.cursor()


url = ""

import requests
# Gets the JSON code off of the website
jsonData = requests.get(url)
# Converts the JSON into a Python list (array)
dataArray = jsonData.json()


userInput = input("What is your favourite number?")
try:
    total += int(userInput)
except TypeError:
    print("You did not enter a number!")


print("Lines should not exceed 79 characters long ")

import math
aNumber = math.factorial(5)

"""