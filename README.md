# REPG小工具
[更新日志](./updatalog.md)

### 功能：
1. 将phi自制铺的 info.csv 转为 info.txt 以让 RE:Phigros 正常显示信息  
    > 悲报：在该功能完成制作后30分钟左右后REP表示将在下个版本添加对info.csv的支持  
    *<del>哼哼，啊啊啊啊啊啊啊（114514）</del>*
    又悲报：REPG开发者因学业繁忙，REPG会停更一段时间

### 将要添加的功能
1. 添加基于Qt的UI界面

### 使用方法
+ 使用python直接运行脚本
    1. 安装`chardet`库
        > 使用`pip install chardet`命令安装`chardet`库
    2. 在本仓库/Releases中下载`main.py`或clone本仓库(建议在Releases中下载`main.py`)
    3. 运行！
+ 直接运行通过pyinstaller打包好的exe可执行文件
    > *comeing soon*

### 注意事项
info.csv 转 info.txt 功能仅支持以下类型的 info.csv
```
Chart,Music,Image,AspectRatio,ScaleRatio,GlobalAlpha,Name,Level,Illustrator,Designer
谱面,音乐,图片,宽高比,按键缩放,背景变暗,名称,等级,曲绘,谱师
22403977.json,22403977.mp3,22403977.jpg,1.777778,8.00E+03,0.6,Name,Level,Illustrator,Designer
```
```
Chart,Music,Image,AspectRatio,ScaleRatio,GlobalAlpha,Name,Level,Illustrator,Designer
22403977.json,22403977.mp3,22403977.jpg,1.777778,8.00E+03,0.6,Name,Level,Illustrator,Designer
```
请确保csv文件最后一行的最后一个项为谱师，倒数第二个项为曲师，倒数第三个项为等级，倒数第四个项为名称  
不支持乱序！！！