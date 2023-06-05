import tkinter as tk
from tkinter import *

# 创建文本框  
root = tk.Tk()
text = tk.Text(root)
text.pack()

# 获取光标所在位置  
cursor_index = text.index(INSERT)
print("光标所在位置：", cursor_index)

root.mainloop()