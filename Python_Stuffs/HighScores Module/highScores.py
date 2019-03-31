"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
# import ref
# import random
# import getpass
# import appJar

letter_to_display = "d"
letter_to_save = "s"

def main(highScore, name):
    option = input("Would you like to display all highscores [" + letter_to_display + "] or add one [" + letter_to_save + "]?")
    if option == letter_to_display:
        try:
            with open("highScores_{}.txt".format(__name__), "r") as file:
                for line in file:
                    data = line.split(",")
                    print(data[0] + ": " + data[1])
        except FileNotFoundError:
                print("404: File Not Found")
    elif option == letter_to_save:
        with open("highScores_{}.txt".format(__name__), "w+") as file:
            for line in file:
                data = line.split(",")
                if data[1] > highScore:
                    data[1] = highScore
                    data[0] = name
                else:
                    n


if __name__ == "__main__":
    main(1000000000, "james")