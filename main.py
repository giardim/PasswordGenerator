from tkinter import *
from generatePassword import *

def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Password Generator")
    spChar = IntVar()
    num = IntVar()
    cap = IntVar()
    lower = IntVar()

    title = Label(text = "Password Generator", font = 15)
    title.place(x = 150, y = 5)

    explainSlider = Label(text = "Password Length?", font = 10)
    explainSlider.place(x = 50, y = 75)

    psswrdLength = Scale(root, from_= 1, to = 32, orient = HORIZONTAL, sliderlength = 15, length = 300, bg = "black", fg = "white")
    psswrdLength.place(x = 50, y = 100)

    askSpecialChar = Checkbutton(root, text = "Special Characters?", variable = spChar, font = 10)
    askSpecialChar.place(x = 50, y = 150)

    askNum = Checkbutton(root, text = "Numbers?", variable = num, font = 10)
    askNum.place(x = 50, y = 200)

    askCapital = Checkbutton(root, text = "Capital Letters?", variable = cap, font = 10)
    askCapital.place(x = 50, y = 250)

    askLower = Checkbutton(root, text = "Lowercase?", variable = lower, font = 10)
    askLower.place(x = 50, y = 300)

    quit = Button(root, text = "Quit", command = lambda:(root.destroy()), padx = 10, pady = 10, font = 10, bg = "black", fg = "orange")
    quit.place(x = 400, y = 400)

    createPword = Button(root, text = "Generate Password", command = lambda:(generatePassword(psswrdLength.get(), spChar.get(), num.get(), cap.get(), lower.get())), padx = 10, pady = 10, font = 10, bg = "black", fg = "orange")
    createPword.place (x = 50, y = 400)

    root.mainloop()

main()