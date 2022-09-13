import os

# list = os.listdir(os.getcwd())
# print("目录")
# print(list)
#
# for path in list:
#     if path == ".idea" or path == "rename.py":
#         continue
#     list2 = os.listdir(path)
#     for dir in list2:
#         # os.rename()
#         print(dir + " rename to :" + path + "_" + dir)
#         # print(path.)
#         os.rename(path + "/" + dir, "newPath/" + path + "_" + dir)
import shutil


# parent = "I:\仓库\本\合集\JIMA"
# list = os.listdir(parent)
# for path in list:
#     if path == "PDF":
#         continue
#     # print("list:"+path)
#     list2 = os.listdir(parent + "\\" + path)
#     for dir in list2:
#         asbp = parent + "\\" + path + "\\" + dir
#         asbnp = parent + "\\" + "PSD" + "\\" + path + "\\" + dir
#         if os.path.isdir(asbp):
#             print("二级文件" + asbp)
#             list3 = os.listdir(asbp)
#             for dir2 in list3:
#                 if dir.endswith(".psd"):
#                     print(asbp + "\\" + dir2)
#                     print(asbnp + "\\" + dir2)
#                     if not os.path.exists(asbnp):
#                         os.makedirs(asbnp)
#                     shutil.move(asbp + "\\" + dir2, asbnp + "\\" + dir2)
#         else:
#             if dir.endswith(".psd"):
#                 print(asbp)
#                 print(asbnp)
#                 if not os.path.exists(asbnp.replace(dir, "")):
#                     os.makedirs(asbnp.replace(dir, ""))
#                 shutil.move(asbp, asbnp)


# parent="I:\仓库\本\合集\JIMA"
# list = os.listdir(parent)
# print("目录")
# print(list)
# print(parent+"/"+dir[8:])
# if dir[8:].endswith(".psd"):
# print(dir[8:]+"\n")
# os.rename(parent+"/"+dir, parent+"/"+dir[8:])


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


rawPath = "I:\仓库\本\合集\JIMA"
aimPath = "I:\仓库\本\合集\JIMA\PSD"
extractFiles(rawPath, aimPath, ".psd")
print("finish")
