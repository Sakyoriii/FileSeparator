import os
import shutil
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory
# windnd，桌面拖拽识别路径的库

import windnd


def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    # 弹窗
    showinfo('您拖放的文件', msg)
    path.set(msg)
    path2.set(msg + "\\PSD")


def select_path():
    path_ = askdirectory().replace("/", "\\")
    path.set(path_)


def select_aim():
    path_ = askdirectory().replace("/", "\\")
    path2.set(path_)


def getAsbPath(g_path, ex_path):
    list = os.listdir(g_path)
    files = []
    for dir in list:
        if os.path.isdir(g_path + "\\" + dir):
            if g_path + "\\" + dir == ex_path:
                continue
            files += getAsbPath(g_path + "\\" + dir, ex_path)
        else:
            files.append(g_path + "\\" + dir)
    return files


def extractFiles(e_path, new_path, end):
    e_path = e_path.get()
    new_path = new_path.get()
    end = end.get()
    asb = getAsbPath(e_path, new_path)
    for file in asb:
        if file.endswith(end):
            if ex_tree.get():
                new_file = file.replace(e_path, new_path)
            else:
                new_file = new_path+"\\"+os.path.basename(file)
            parent = os.path.dirname(new_file)

            if not os.path.exists(parent):
                os.makedirs(parent)
            shutil.move(file, new_file)
    # 弹窗
    showinfo("DONE !", "整完了")


def dash():
    extractFiles(path, path2, suffix)


tk = Tk()
# 正常选择按钮打开文件
path = StringVar()
path2 = StringVar()
suffix = StringVar()
ex_tree = BooleanVar()

Label(tk, text="源文件路径:").grid(row=0, column=0)
Entry(tk, textvariable=path).grid(row=0, column=1)
Button(tk, text="路径选择", command=select_path).grid(row=0, column=2)
# 拖拽文件

Label(tk, text="输出路径:").grid(row=1, column=0)
Entry(tk, textvariable=path2).grid(row=1, column=1)
Button(tk, text="路径选择", command=select_aim).grid(row=1, column=2)

Label(tk, text="文件后缀:").grid(row=2, column=0)
Entry(tk, textvariable=suffix).grid(row=2, column=1)
suffix.set(".psd")
Button(tk, text="Go", command=dash).grid(row=3,column=0)

Checkbutton(tk, text="输出父路径", variable=ex_tree).grid(row=3, column=1)

windnd.hook_dropfiles(tk, func=dragged_files)
tk.mainloop()
