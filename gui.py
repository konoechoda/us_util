import tkinter as tk
import threading
from app.copyUtil.__init__ import starter as copyUtil_starter
from app.deleteEmptyFoldersUtil.__init__ import starter as deleteEmptyFoldersUtil_starter


class StartupPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("瞅瞅?有啥好玩的")
        self.geometry("300x200")

        # 创建按钮并绑定点击事件
        self.start_copy_util_btn = tk.Button(self, text="同类型文件批量拷贝", command=self.start_copy_util)
        self.start_copy_util_btn.pack(pady=20)

        self.start_delete_empty_folders_util_btn = tk.Button(self, text="空文件夹批量删除",
                                                             command=self.start_delete_empty_folders_util)
        self.start_delete_empty_folders_util_btn.pack(pady=20)

    def start_copy_util(self):
        """
        启动复制工具函数，并隐藏启动页面。
        """
        self.withdraw()  # 隐藏启动页面
        threading.Thread(target=self.run_copy_util).start()

    def start_delete_empty_folders_util(self):
        """
        启动删除空文件夹工具函数，并隐藏启动页面。
        """
        self.withdraw()  # 隐藏启动页面
        threading.Thread(target=self.run_delete_empty_folders_util).start()

    def run_copy_util(self):
        """
        执行复制工具的启动函数，并在脚本完成后再次显示启动页面。
        """
        copyUtil_starter()  # 调用复制工具的启动函数
        self.deiconify()  # 脚本完成后再次显示启动页面

    def run_delete_empty_folders_util(self):
        """
        执行删除空文件夹工具的启动函数，并在脚本完成后再次显示启动页面。
        """
        deleteEmptyFoldersUtil_starter()  # 调用删除空文件夹工具的启动函数
        self.deiconify()  # 脚本完成后再次显示启动页面
