from tkinter import *
import webbrowser
from SelfDefineTool import *


class ContentFrame:
    def __init__(self, master):
        self.frame = Frame(master)
        self.setFrameInfo()

    def setFrameInfo(self):
        def refreshFrame():
            content = t1.get("1.0", "end")
            with open(file="Contents.txt", mode="w", encoding="utf-8") as f:
                f.write(content)
            run()
            webbrowser.open("沉浸翻译.html")

        font = ("微软雅黑", 12, "bold")
        t1 = Text(self.frame, font=font, width=120)
        t1.pack()
        b1 = Button(self.frame, text='刷新网页', font=font, background="green", command=refreshFrame)
        b1.pack()

    def own_frame(self):
        return self.frame


class Face:
    def __init__(self):
        self.root = Tk()
        self.setAttribute()
        self.setMenu()
        self.current: Frame = Frame()
        self.root.mainloop()

    def setAttribute(self):
        self.root.title("翻译")
        w = 1200
        h = 700
        area = (
            w, h, int((self.root.winfo_screenwidth() - w) / 2),
            int((self.root.winfo_screenheight() - h) / 2))
        self.root.geometry("{}x{}+{}+{}".format(*area))

    def setMenu(self):
        def showContentFrame():
            content_frame = ContentFrame(self.root)
            if self.current != content_frame.own_frame():
                self.current.pack_forget()
                self.current = content_frame.own_frame()
                self.current.pack()

        main_menu = Menu(self.root)
        main_menu.add_command(label="文本界面", command=showContentFrame)
        self.root.config(menu=main_menu)


if __name__ == '__main__':
    face = Face()
