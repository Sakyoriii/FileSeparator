import os
import re

# str = '[2022-02-06] 高画質版、黒線修正版'
#
# print(str.__contains__('\[20[1,2]\d-\d{1,2}-\d{1,2}]'))
#
#
#
# print(re.match('\[20[1,2]\d-\d{1,2}-\d{1,2}]',str))
# print(re.match('\[20[1,2]\d-\d{1,2}-\d{1,2}]',str).group())
import shutil


def sameDate(file1, file2):
    matchStr = '\[20[1,2]\d-\d{1,2}-\d{1,2}]'  # 关键词正则匹配，
    date1 = re.match(matchStr, file1).group()
    date2 = re.match(matchStr, file2).group()
    return date1 == date2  # 把匹配到的部分进行比对


path = r'C:\Users\\75219\Downloads\\tmp\kuja'   # 工作路径

list = os.listdir(path)
mainKey = '高'
attachKey = '高'
prfx4attach = 'Attach_'
# files = []
for file1 in list:
    if not file1.__contains__(attachKey):   # 遍历主文件夹
        for file2 in list:
            if file2.__contains__(attachKey):   # 遍历附加文件夹
                if sameDate(file1, file2):      # 比对主附一致
                    print(file1, '=', file2)
                    filelist = os.listdir(path + '\\' + file2)
                    # print('list:',filelist)
                    for item in filelist:
                        print(path + '\\' + file2 + '\\' + item)
                        # 重命名文件加上前缀避免移动时出现重复
                        os.rename(path + '\\' + file2 + '\\' + item, path + '\\' + file2 + '\\' + prfx4attach + item)
                        # 移动附加文件到主文件夹
                        shutil.move(path + '\\' + file2 + '\\' + prfx4attach + item, path + '\\' + file1)
                    # 移除已空的附加文件夹
                    os.rmdir(path + '\\' + file2)

# print(list)
