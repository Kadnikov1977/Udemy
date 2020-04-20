from tkinter import *

root_window = Tk()

root_window.geometry('500x500')
root_window.title('Welcome screen')

hello_label = Label(root_window, text = 'Hello World!!!', font = ('arial', 20, 'bold'), fg = 'green', bg = 'blue')
# hello_label.pack() # Сверху по центру распологает виджеты
hello_label.place(x = 500/2 - hello_label.winfo_reqwidth()/2, y = 500/2 - hello_label.winfo_reqheight()/2)

go_button = Button(root_window, text = 'Click me!!!')
go_button.place(x = 500/2 - go_button.winfo_reqwidth()/2, y = 500*3/4 - go_button.winfo_reqheight()*3/4)
go_button.
root_window.mainloop()
