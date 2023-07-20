import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    x=random.randint(1,9)
    x2 = random.randint(1, 9)
    x3 = random.randint(1, 9)
    x4 = random.randint(1, 9)
    x5 = random.randint(1, 9)
    x6 = random.randint(1, 9)

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    messagebox.showinfo(title="lottery ticket", message=(str(x) )+(str(x2) )+(str(x3) )+(str(x4) )+(str(x5) )+(str(x6) ))
    window.mainloop()
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
