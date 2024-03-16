import tkinter as tk
from app.copyUtil.gui import FileCopierGUI


def starter():
    """
    程序启动函数，创建并运行文件拷贝工具的图形用户界面

    该函数创建一个 Tkinter 窗口，并将文件拷贝工具的图形用户界面添加到窗口中，
    然后启动 Tkinter 主循环以显示界面并等待用户交互。
    """
    # 创建一个 Tkinter 窗口对象
    window = tk.Tk()
    # 设置窗口标题
    window.title("同类型文件批量拷贝工具")
    # 设置窗口初始大小
    window.geometry("500x450")

    # 创建文件拷贝工具的图形用户界面，并将窗口作为其父组件
    FileCopierGUI(window)

    # 进入 Tkinter 主循环，显示界面并等待用户交互
    window.mainloop()
