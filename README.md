# py-to-exe_by-pyinstaller
通过cmd中的pyinstaller.exe将py文件转化成exe文件  

使用前请确保：  
py文件在一个文件夹内，且文件夹内除了py和ico文件没有其他文件  
选择文件前请先看终端显示的文字，避免选错  
  
此程序需要pyinstaller，请确保cmd提前pip install pyinstaller过，若没有检测到已安装pyinstaller，你可以选择回答Y来安装，也可以回答N退出程序  

程序运行完成后，若最后一个信息显示：  
Building EXE from EXE-00.toc completed successfully  
则表示打包成功  
请回到文件夹，打开里面的dist文件夹，即可拿到exe文件
