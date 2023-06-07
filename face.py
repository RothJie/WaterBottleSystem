from tkinter import *
import webbrowser
from engine import *


class RocketFrame:
    def __init__(self, root):
        self.root = root

    def get(self):
        # 绑定事件一定要传入event
        def show_hand_cursor(event):
            t1.config(cursor='arrow')

        def show_xterm_cursor(event):
            t1.config(cursor='xterm')

        links = {}

        def click(event):
            r = int(t1.index(INSERT).split(".")[0]) + 1  # 获取光标所在的行列信息
            if r not in links:
                r = 2
            webbrowser.open(links[r])

        frame = Frame(self.root)
        l1 = Label(frame, text="火箭发射界面", foreground="purple", font=("黑体", 15, "bold"))
        l1.pack()
        t1 = Text(frame, width=65, height=25, font=("黑体", 15, "bold"))
        contents = hangQingUrl("火箭发射")[0]
        params = hangQingUrl("火箭发射")[1]
        sql = 'insert into rocket values(%s,%s,%s);'
        dataToMysql(params=params, sql=sql)
        # print(contents)

        str_info = f"股票代码\t基本信息\n"
        t1.insert(f"1.0", str_info)
        line = 2
        for co in contents:
            str_info = f"{co}\t{contents[co][1]}\n"
            t1.insert(f"{line}.0", str_info)
            t1.tag_add("link", f"{line}.0", f"{line}.6")
            t1.tag_config('link', foreground='red', underline=True)
            links[line] = contents[co][0]
            line += 1
        t1.tag_bind('link', '<Enter>', show_hand_cursor)
        t1.tag_bind('link', '<Leave>', show_xterm_cursor)
        t1.tag_bind('link', '<Button-1>', click)
        t1.pack()
        return frame


class BigBuyFrame:
    def __init__(self, root):
        self.root = root

    def get(self):
        # 绑定事件一定要传入event
        def show_hand_cursor(event):
            t1.config(cursor='arrow')

        def show_xterm_cursor(event):
            t1.config(cursor='xterm')

        links = {}

        def click(event):
            r = int(t1.index(INSERT).split(".")[0]) + 1  # 获取光标所在的行列信息
            if r not in links:
                r = 2
            webbrowser.open(links[r])

        frame = Frame(self.root)
        l1 = Label(frame, text="大笔买入界面", foreground="purple", font=("黑体", 15, "bold"))
        l1.pack()
        t1 = Text(frame, width=65, height=25, font=("黑体", 15, "bold"))
        contents = hangQingUrl("大笔买入")[0]
        params = hangQingUrl("大笔买入")[1]
        sql = 'insert into bigbuy values(%s,%s,%s);'
        dataToMysql(params=params, sql=sql)
        # print(contents)

        str_info = f"股票代码\t基本信息\n"
        t1.insert(f"1.0", str_info)
        line = 2
        for co in contents:
            str_info = f"{co}\t{contents[co][1]}\n"
            t1.insert(f"{line}.0", str_info)
            t1.tag_add("link", f"{line}.0", f"{line}.6")
            t1.tag_config('link', foreground='red', underline=True)
            links[line] = contents[co][0]
            line += 1
        t1.tag_bind('link', '<Enter>', show_hand_cursor)
        t1.tag_bind('link', '<Leave>', show_xterm_cursor)
        t1.tag_bind('link', '<Button-1>', click)
        t1.pack()
        return frame


class CompeteUpFrame:
    def __init__(self, root):
        self.root = root

    def get(self):
        # 绑定事件一定要传入event
        def show_hand_cursor(event):
            t1.config(cursor='arrow')

        def show_xterm_cursor(event):
            t1.config(cursor='xterm')

        links = {}

        def click(event):
            r = int(t1.index(INSERT).split(".")[0]) + 1  # 获取光标所在的行列信息
            if r not in links:
                r = 2
            webbrowser.open(links[r])

        frame = Frame(self.root)
        l1 = Label(frame, text="竞价上涨界面", foreground="purple", font=("黑体", 15, "bold"))
        l1.pack()
        t1 = Text(frame, width=65, height=25, font=("黑体", 15, "bold"))
        contents = hangQingUrl("竞价上涨")[0]
        params = hangQingUrl("竞价上涨")[1]
        sql = 'insert into morning_compete_up values(%s,%s,%s);'
        dataToMysql(params=params, sql=sql)

        str_info = f"股票代码\t基本信息\n"
        t1.insert(f"1.0", str_info)
        line = 2
        for co in contents:
            str_info = f"{co}\t{contents[co][1]}\n"
            t1.insert(f"{line}.0", str_info)
            t1.tag_add("link", f"{line}.0", f"{line}.6")
            t1.tag_config('link', foreground='red', underline=True)
            links[line] = contents[co][0]
            line += 1
        t1.tag_bind('link', '<Enter>', show_hand_cursor)
        t1.tag_bind('link', '<Leave>', show_xterm_cursor)
        t1.tag_bind('link', '<Button-1>', click)
        t1.pack()
        return frame


class Face:
    def __init__(self):
        self.root = Tk()
        self.rocket_frame = RocketFrame(self.root)
        self.big_buy_frame = BigBuyFrame(self.root)
        self.competeUp_frame = CompeteUpFrame(self.root)
        self.setAttribute()
        self.currentFrame: Frame = Frame()
        self.setMenuBlank()
        self.root.mainloop()

    def setAttribute(self):
        self.root.title('轻松看盘')
        w = 850
        h = 800
        s_w = self.root.winfo_screenwidth()
        s_h = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (w, h, int((s_w - w) / 2), int((s_h - h) / 2)))

    def setMenuBlank(self):
        def rocket():
            if self.currentFrame != self.rocket_frame.get():
                self.currentFrame.pack_forget()
                self.currentFrame = self.rocket_frame.get()
                self.currentFrame.pack()

        def bigBuy():
            if self.currentFrame != self.big_buy_frame.get():
                self.currentFrame.pack_forget()
                self.currentFrame = self.big_buy_frame.get()
                self.currentFrame.pack()

        def competeUp():
            if self.currentFrame != self.competeUp_frame.get():
                self.currentFrame.pack_forget()
                self.currentFrame = self.competeUp_frame.get()
                self.currentFrame.pack()

        menu = Menu(self.root)
        menu.add_command(label='火箭发射', command=rocket)
        menu.add_command(label='大笔买入', command=bigBuy)
        menu.add_command(label='竞价上涨', command=competeUp)
        self.root.config(menu=menu)


if __name__ == '__main__':
    face = Face()
