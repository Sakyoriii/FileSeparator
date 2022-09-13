import os
import shutil
import tkinter as tk
from tkinter import filedialog


def getAsbPath(path):
    list = os.listdir(path)
    files = []
    for dir in list:
        if os.path.isdir(path + "\\" + dir):
            files += getAsbPath(path + "\\" + dir)
        else:
            files.append(path + "\\" + dir)
    return files


def extractFiles(path, new_path, end):
    asb = getAsbPath(path)
    for file in asb:
        if file.endswith(end):
            new_file = file.replace(path, new_path)
            parent = os.path.dirname(new_file)

            if not os.path.exists(parent):
                os.makedirs(parent)
            shutil.move(file, new_file)
    return "done"


root = tk.Tk()
root.withdraw()
file_path = ""
while not os.path.isdir(file_path):
    input("选择正确文件路径(回车键继续）") == "y"
    # 获取文件路径
    file_path = filedialog.askdirectory()

    print(file_path)

aimPath = file_path + "\\PSD"
# print(file_path)
print("是否设定psd路径（默认文件路径下PSD文件夹内）")
new_path = input("[y/n]回车使用默认")
if not new_path == "y":
    # do something
    aimPath = filedialog.askdirectory()
print(aimPath)
end = input("请输入替换文件后缀,默认\".psd\"（回车）")
if end == "":
    print("suffix:.psd")
    print(extractFiles(file_path, aimPath, ".psd"))
else:
    print("suffix:"+end)
    print(extractFiles(file_path, aimPath, end))
