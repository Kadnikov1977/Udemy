from tkinter import *

main_window = Tk()
main_window.geometry('800x600+100+100')

# my_label = Label(main_window, text = 'My text', bg = 'white')
# my_label.pack(fill = X)
# my_label.pack(fill = X, expand = 1)
# my_label.pack(fill = Y, expand = 1)
# my_label.pack(fill = BOTH, expand = 1)
red_label = Label(main_window, text = 'RED', bg = 'red')
red_label.pack(fill = BOTH, expand = 1, padx = 10, pady = 10)

yellow_label = Label(main_window, text = 'YELLOOW', bg = 'yellow')
yellow_label.pack(fill = BOTH, expand = 1, padx = 10, pady = 10)

blue_label = Label(main_window, text = 'BLUE', bg = 'blue')
blue_label.pack(fill = BOTH, expand = 1, padx = 10, pady = 10)




main_window.mainloop()