##################################
#A program that allows the user to make decisions
#   regarding what type of password they want
#   then returns a randomly generated password
#Written by Michael Giardina
#Python 3.9.1
#30 OCT 2022
##################################

from tkinter import *
from generatePassword import *

def main():
    #set up variables
    root = Tk()
    root.geometry("500x500")
    root.title("Password Generator")
    spChar = IntVar()
    num = IntVar()
    cap = IntVar()
    lower = IntVar()

    #Put a title at the top of the window
    title = Label(text = "Password Generator", font = 15)
    title.place(x = 150, y = 5)

    #explain what the slider does
    explainSlider = Label(text = "Password Length", font = 10)
    explainSlider.place(x = 50, y = 75)

    #puts the slider on the screen
    psswrdLength = Scale(root, from_= 1, to = 32, orient = HORIZONTAL, sliderlength = 15, length = 300, bg = "black", fg = "white")
    psswrdLength.place(x = 50, y = 100)

    #ask the user if they want special characters in their password
    askSpecialChar = Checkbutton(root, text = "Special Characters", variable = spChar, font = 10)
    askSpecialChar.place(x = 50, y = 150)

    #ask the user if they want numbers in their password
    askNum = Checkbutton(root, text = "Numbers?", variable = num, font = 10)
    askNum.place(x = 50, y = 200)

    #ask the user if they want capital letters in their password
    askCapital = Checkbutton(root, text = "Capital Letters?", variable = cap, font = 10)
    askCapital.place(x = 50, y = 250)

    #ask the user if they want lowercase letters in their password
    askLower = Checkbutton(root, text = "Lowercase?", variable = lower, font = 10)
    askLower.place(x = 50, y = 300)

    #place a button that allows the user to quit the program
    quit = Button(root, text = "Quit", command = lambda:(root.destroy()), padx = 10, pady = 10, font = 10, bg = "black", fg = "orange")
    quit.place(x = 400, y = 400)

    #place a button that generates the password when clicked
    createPword = Button(root, text = "Generate Password", command = lambda:(generatePassword(psswrdLength.get(), spChar.get(), num.get(), cap.get(), lower.get())), padx = 10, pady = 10, font = 10, bg = "black", fg = "orange")
    createPword.place (x = 50, y = 400)

    #keep the program running
    root.mainloop()

#call main function
main()