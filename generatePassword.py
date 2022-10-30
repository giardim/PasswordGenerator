##################################
#A program that generates a random password
#   and saves it in a file
#Written by Michael Giardina
#Python 3.9.1
#30 OCT 2022
##################################

import random

class generatePassword:
    def __init__(self, pLength, specialChar, num, cap, low):
        #set up variables
        specialList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        capList = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.pLength = pLength
        self.specialChar = specialChar
        self.num = num
        self.cap = cap
        self.low = low
        password = ""
        f = open("password.txt", "a")

        #Make sure atleast one perameter is passed with a valid number
        if (not specialChar and not num  and not cap and not low):
            pLength = 0
            f.write("You need to select atleast one option")

        #While the password length the user requested is 
        #   greater than 0
        while (pLength > 0):
            #get a random integer, this will determine
            #   what list to take a character from
            randInt = random.randint(0, 3)
            #if the random integer is 0
            if (randInt == 0 and specialChar):
                #take a random character from the special list 
                #   and decrement the password length
                password += random.choice(specialList)
                pLength -= 1
            #if the random integer is 1
            elif (randInt == 1 and num):
                #take a random character from the number list 
                #   and decrement the password length
                password += random.choice(numList)
                pLength -= 1
            #if the random integer is 2
            elif (randInt == 2 and cap):
                #take a random character from the special list 
                #   and decrement the capital letters list
                password += random.choice(capList)
                pLength -= 1
            #if the random integer is 3
            elif (randInt == 3 and low):
                #take a random character from the lowercase letters list 
                #   and decrement the password length
                password += random.choice(lowList)
                pLength -= 1
        #add a new line escape sequence to the end of the password
        password += "\n"
        
        #save the password to the file
        f.write(password)