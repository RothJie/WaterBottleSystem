import tkinter.messagebox
from tkinter import *


class Face:
    def __init__(self):
        self.root = tkinter.Tk()
        self.setAttribute()
        self.root.mainloop()

    def setAttribute(self):
        self.root.title('大单动向')
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        f_w = 700
        f_h = 700
        self.root.geometry("%dx%d+%d+%d" % (f_w, f_h, int((w - f_w) / 2), int((h - f_h) / 2)))

    def mainMenu(self):
        main_menu = Menu(self.root)
        main_menu.add_command()
        main_menu.pack()


face = Face()
