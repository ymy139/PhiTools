# 导库
import csv
import os
import chardet
import sys
import time
# 打开输出记录文件
OutFile = open("ChangeLog.txt", "w", encoding="utf-8")
# info.csv 转 info.txt 功能函数
def csv_to_txt(chartpath: str, loglevel: int):
    OutFile.write("转换日志\n功能: info.csv 转 info.txt\n\n")
    # 切换目录
    os.chdir(chartpath)
    # 获取文件夹列表
    DirList = os.listdir()
    # 获取文件夹数目
    DirCount = len(DirList)
    # 主循环,循环 文件夹数 次,并将循环次数保存至变量 i
    for i in range(DirCount):
        try:
            # 切换到铺面目录
            os.chdir(DirList[i])
        # 如果不是一个目录...
        except NotADirectoryError:
            # 输出错误
            print_log(DirList[i]+" 不是一个目录, 进行下一次循环", "ERROR")
            # 记录错误
            OutFile.write(DirList[i]+" 不是一个目录, 进行下一次循环\n")
            # 进入下一次循环
            continue
        if loglevel < 3:
            # 输出工作路径
            print_log("开始转换铺面info: 在: "+os.getcwd()+" 的铺面info", "INFO")
            # 记录工作路径
            OutFile.write("开始转换铺面info: 在: "+os.getcwd()+" 的铺面info\n")
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
            print_log("铺面路径 "+os.getcwd()+" 没有info.csv文件,开始下一个目录的转换", "WRAN")
            OutFile.write("铺面路径 "+os.getcwd()+" 没有info.csv文件,开始下一个目录的转换\n")
        # 如果有csv文件...
        if HaveCSV == True:
            # 建立/重置二维列表用于存放csv读取出来的数据
            CSVData = []
            # 读取csv
            Reader = csv.reader(CSVFile)
            # 输出内容
            for row in Reader:
                if loglevel < 2:
                    # 输出数据
                    print_log("获取到csv数据: "+str(row), "DEBUG")
                    # 记录数据
                    OutFile.write("获取到csv数据: "+str(row)+"\n")
                # 存放数据
                CSVData.append(row)
            # 关闭csv
            CSVFile.close()
            # 建立/打开info.txt
            TXTFile = open("info.txt", "w", encoding="utf-8")
            # 读取基本信息
            LevelDesigner = CSVData[-1][-1]
            Composer = CSVData[-1][-2]
            Level = CSVData[-1][-3]
            Name = CSVData[-1][-4]
            # 写入
            TXTFile.write("#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner+"\n")
            # 记录
            if loglevel < 2:
                OutFile.write("写入数据: \n#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner+"\n")
                print_log("写入：\n#\nName: "+Name+"\nLevel: "+Level+"\nComposer: "+Composer+"\nCharter: "+LevelDesigner, "DEBUG")
        # 回到存放铺面的总文件夹
        os.chdir("..")
# 退出函数
def exit_program(exitcode: int = 0):
    # 关闭输出记录文件
    OutFile.close()
    # 退出
    sys.exit(exitcode)
# log输出函数
def print_log(text: str, loglevel: str):
    print("["+time.strftime("%H:%M:%S")+"] ["+loglevel+"] "+text)
# 主交互逻辑
def main():
    # 清屏
    os.system("cls")
    # 输出信息
    print("REPGTools v0.1.0   by: ymy139   github: https://github.com/ymy139/REPGTools")
    print("欢迎使用REPGTools, 请输入您要进行的操作：")
    print("    1. info.csv 转 info.txt")
    print("    0. 退出")
    print(" ")
    while True:
        # 获取用户输入--功能编号
        user_input = input("输入功能编号:")
        # 尝试将用户输入转换为int类型
        try:
            user_input = int(user_input)
            # 成功转换则跳出循环
            break
        except:
            # 否则提示
            print_log("虽然不知道你输入的是啥, 但肯定不是阿拉伯数字, 对吧?", "WRAN")
    while True:
        # 获取用户输入--日志等级
        loglevel = input("输入日志等级(1. 详细, 2.一般,3. 仅输出警告):")
        # 尝试将用户输入转换为int类型
        try:
            loglevel = int(loglevel)
            # 成功转换则跳出循环
            break
        except:
            # 否则提示
            print_log("虽然不知道你输入的是啥, 但肯定不是阿拉伯数字, 对吧?", "WRAN")
    if user_input == 1:
        while True:
            # 获取用户输入--铺面路径
            chartpath = input("输入存放铺面文件夹目录的绝对路径：")
            # 检查目录是否存在
            if os.path.exists(chartpath) == True:
                # 存在则跳出循环
                break
            else:
                # 否则提示
                print_log("皇帝的新目录? (请检查输入的路径或检查路径是否损坏)", "WRAN")
        # 执行csv_to_txt函数
        csv_to_txt(chartpath, loglevel)
    if user_input == 0:
        # 执行退出函数
        exit_program()
# 执行主函数
main()