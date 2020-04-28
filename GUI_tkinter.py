from tkinter import *

root_window = Tk()

root_window.geometry('1920x1080')
root_window.title('Welcome screen')

hello_label = Label(root_window, text = 'Hello World!!!', font = ('arial', 20, 'bold'), fg = '#FF1593', bg = '#FF9900')
# hello_label.pack() # Сверху по центру распологает виджеты
hello_label.place(x = 1920/2 - hello_label.winfo_reqwidth()/2, y = 1080/2 - hello_label.winfo_reqheight()/2)

go_button = Button(root_window, text = 'Click me!!!')
go_button.place(x = 1920/2 - go_button.winfo_reqwidth()/2, y = 1080*3/4 - go_button.winfo_reqheight()*3/4)

root_window.mainloop()
