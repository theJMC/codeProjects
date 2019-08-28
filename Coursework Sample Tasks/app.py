"""
Name: Programming Project (SAMPLE TASK) -- App Module

Date: 25/08/2019

Author: _TheJMC_ (github.com/TheJMC)

Notes:


"""

# Imports

import getpass # Password Blanking input
import csv # CSV file manipulation library

# Variables

student_file = "students.csv"
students = []

# Classes



# Functions / Procedues

def refreshStudents():
    # Opens {student_file} and loads them into the 2D array students
    with open(student_file, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append(row)
        print(students[0])

def main():
    refreshStudents()


# Only run main() if program is running locally, not imported.
if __name__ == "__main__":
    main()


