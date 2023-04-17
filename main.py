CHART_PATH = "D:\\铺面\\Phigros\\Unzip"
# 导库
import csv
import os
import chardet
# 打开输出记录文件
OutFile = open("out.txt", "w", encoding="utf-8")
# 切换目录
os.chdir(CHART_PATH)
# 获取文件夹列表
DirList = os.listdir()
# 获取文件夹数目
DirCount = len(DirList)
# 主循环,循环 文件夹数 次,并将循环次数保存至变量 i
for i in range(DirCount):
    # 切换到铺面目录
    os.chdir(DirList[i])
    # 尝试...
    try:
        # 以二进制打开csv
        CSVFile = open("info.csv", "rb")
        # 获取编码
        Encoding = chardet.detect(CSVFile.read())["encoding"]
        # 关闭文件
        CSVFile.close()
        # 使用对应编码打开csv
        CSVFile = open("info.csv", "r", encoding=Encoding)
        # 有csv文件,将HaveCSV设为True
        HaveCSV = True
    # 否则...
    except:
        # 如果没有csv文件,则将HaveCSV设为False
        HaveCSV = False
    # 如果有csv文件...
    if HaveCSV == True:
        # 输出工作路径
        print(os.getcwd()+"\n")
        # 记录工作路径
        OutFile.write(os.getcwd()+"\n")
        # 建立/重置二维列表用于存放csv读取出来的数据
        CSVInfo = []
        # 读取csv
        Reader = csv.reader(CSVFile)
        # 输出内容
        for row in Reader:
            # 输出数据
            print(row)
            # 记录数据
            OutFile.write(str(row)+"\n")
            # 存放数据
            CSVInfo.append(row)
        # 关闭csv
        CSVFile.close()
        # 换行
        print("\n")
        OutFile.write("\n")
        # 建立/打开info.txt
        TXTFile = open("info.txt", "w", encoding="utf-8")
        # 读取基本信息
        LevelDesigner = CSVInfo[-1][-1]
        Composer = CSVInfo[-1][-2]
        Level = CSVInfo[-1][-3]
        Name = CSVInfo[-1][-4]
        # 写入
        TXTFile.write("#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner+"\n")
        # 记录
        OutFile.write("写入：\n#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner+"\n\n\n")
        print("写入：\n#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner+"\n\n\n")
    # 回到存放铺面的总文件夹
    os.chdir("..")
# 关闭输出记录文件
OutFile.close()