"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import accounts as a

if __name__ == "__main__":
    db = a.database(input("Please enter name of Database: "))
    db.setupTable()
