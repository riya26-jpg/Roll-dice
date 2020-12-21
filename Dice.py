from tkinter import *
# install PIP tkintertable
import random

root = Tk()
root.title("Roll Dice")
root.geometry("600x600")

label = Label(root, font=('Arial',400, 'bold'), text='')


def rolldice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button = Button(root,font=('helvetica',15,'bold'),text='roll dice',command=rolldice,bg="red")
button.pack()

root.mainloop()
