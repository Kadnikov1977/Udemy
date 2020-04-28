from tkinter import *
import random

root = Tk()
root.geometry('1000x500')

def move(event):
    x1 = random.randint(0,900)
    y1 = random.randint(0,400)
    button1.place(x = x1, y = y1)
    print(x1, y1)
    # s = "Движение мышью {}x{}".format(x, y)
    # root.title(s)
def center(event):
    x1 = 500
    y1 = 250
    button1.place(x=x1, y=y1, anchor = CENTER)


# red_label = Label(root, text = 'RED', bg = 'red')
# red_label.place(x = 50, y = 50)
#
# yellow_label = Label(root, text = 'YELLOOW', bg = 'yellow')
# yellow_label.place(x = 150, y = 150)

button1 = Button(root, text = 'Нажми меня')
button1.place(x = 250, y = 250)
button1.bind('<Motion>', move)

button2 = Button(root, text = 'По центру')
button2.place(x = 900, y = 450)
button2.bind('<ButtonPress>', center)

root.mainloop()