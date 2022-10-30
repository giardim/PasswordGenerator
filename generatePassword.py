import random

class generatePassword:
    def __init__(self, pLength, specialChar, num, cap, low):
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

        if (not specialChar and not num  and not cap and not low):
            pLength = 0
            f.write("You need to select atleast one option")

        while (pLength > 0):
            randInt = random.randint(0, 3)
            if (randInt == 0 and specialChar):
                password += random.choice(specialList)
                pLength -= 1
            elif (randInt == 1 and num):
                password += random.choice(numList)
                pLength -= 1
            elif (randInt == 2 and cap):
                password += random.choice(capList)
                pLength -= 1
            elif (randInt == 3 and low):
                password += random.choice(lowList)
                pLength -= 1
        password += "\n"
        f.write(password)