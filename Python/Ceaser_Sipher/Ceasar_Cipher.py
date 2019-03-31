#-------------------------------------------------------------------------------
# Name:        Caeser Cipher
# Purpose:     Converts a phase to a caesar cipher code
#
# Author:      15mccarthyj
#
# Created:     19/10/2018
# Copyright:   (c) 15mccarthyj 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        rotation = int(input("Please input your rotaion: "))
    except ValueError as e:
        print("Please put in a valid rotation scale!")
        main()
    phrase = input("Please enter your phrase: ").lower()
    newPhrase = list(phrase)
    final = []
    for i in range(0, len(newPhrase)):
        index = alphabet.index(newPhrase[i])
        rotated = index + rotation
        try:
            final.append(alphabet[rotated])
        except IndexError as e:
            rotated = 26 - rotated
            final.append(alphabet[rotated])
        

    converted = ''.join(final)
    print("Output: " + converted)

if __name__ == '__main__':
    main()
