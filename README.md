# REPG小工具
将phi自制铺的 info.csv 转为 info.txt 以让 RE:Phigros 正常显示信息  
悲报：在本脚本完成制作后30分钟左右后REP表示将在下个版本添加对info.csv的支持  
*<del>哼哼，啊啊啊啊啊啊啊（114514）</del>*

## 使用方法
1. 安装`chardet`库
    > 使用`pip install chardet`命令安装`chardet`库
2. 在本仓库/Releases中下载`main.py`或clone本仓库
3. 修改`main.py`中第1行的常量为你存放铺面文件夹的位置
4. 运行！

## 注意事项
本脚本仅支持以下类型的info.csv
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