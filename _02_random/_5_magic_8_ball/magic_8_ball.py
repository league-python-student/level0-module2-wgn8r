import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    ran=random.randint(0,3)
    # If the random number is 0
    if ran==0:
        print("yes")
    if ran == 1:
        print("no")
    if ran == 2:
        print("Maybe you should ask Google?")
    if ran == 3:
        print("50/50 chance")

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
