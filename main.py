import tkinter as tk
import tkinter.filedialog as file
import os
import sys
s = "".join(os.popen("pip list").readlines())
if "pyinstaller  " not in s: #加上空格防止其他命令与pyinstaller重名
    ans = input("你的电脑目前没有pyinstaller，是否现在下载？(Y/N)")
    if ans == "Y":
        os.system("pip install pyinstaller")
    elif ans == "N":
        sys.exit()

print("请将py文件放入一个空文件夹，若要指定exe图标，在文件夹内放入一个ico图标文件")
mode = input("输入i则指定exe图标，输入其他字符则不指定")
if mode == "i":
    print("为保证稳定性，请确保文件夹只有1个py和1个ico文件，只需选择py文件，ico文件将自动检测")
    a = tk.Tk()
    d = file.askopenfilename()
    a.destroy()
    if d[-2:] != "py":
        print("文件选择错误")
        sys.exit()
    dl = d.split("/")
    py = dl[-1]
    d = d.strip(py)
    allfile = os.listdir(d)
    allfile.remove(py)
    ico = allfile[0]
    print("请耐心等待程序运行")
    os.system("cd "+ d +" && pyinstaller -F -i"+ ico +" "+ py)
    print("程序运行完成，若最后一个信息显示：")
    print("Building EXE from EXE-00.toc completed successfully")
    print("则表示打包成功")
    print("请回到文件夹，打开里面的dist文件夹，即可拿到exe文件")
else:
    a = tk.Tk()
    d = file.askopenfilename(filetypes=[("Python文件","*.py")])
    a.destroy()
    if d[-2:] != "py":
        print("文件选择错误")
        sys.exit()
    dl = d.split("/")
    py = dl[-1]
    d = d.strip(py)
    print("请耐心等待程序运行")
    os.system("cd " + d + " && pyinstaller -F "+py)
    print("程序运行完成，若最后一个信息显示：")
    print("Building EXE from EXE-00.toc completed successfully")
    print("则表示打包成功")
    print("请回到文件夹，打开里面的dist文件夹，即可拿到exe文件")
