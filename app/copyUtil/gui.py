import tkinter as tk
import os
from tkinter import filedialog, messagebox
from app.copyUtil.copy_config_params import CopyConfigParams
from app.copyUtil.file_operations import FileOperations


class FileCopierGUI:
    def __init__(self, master):
        # 初始化GUI界面
        self.master = master
        # 创建GUI组件
        self.create_widgets()
        # 初始化拷贝配置参数对象，初始值为空字符串
        self.copyConfigParams = CopyConfigParams("", "", "", "")
        # 刷新单选按钮的选中状态
        self.refresh_radio_buttons()

    def create_widgets(self):
        # 创建源文件夹路径标签和输入框
        self.source_label = tk.Label(self.master, text="源文件夹路径:")
        self.source_label.pack()
        self.source_entry = tk.Entry(self.master)
        self.source_entry.pack()
        # 创建浏览源文件夹路径按钮
        self.source_button = tk.Button(self.master, text="浏览", command=self.browse_source_dir)
        self.source_button.pack()

        # 创建目标文件夹路径标签和输入框
        self.destination_label = tk.Label(self.master, text="目标文件夹路径:")
        self.destination_label.pack()
        self.destination_entry = tk.Entry(self.master)
        self.destination_entry.pack()
        # 创建浏览目标文件夹路径按钮
        self.destination_button = tk.Button(self.master, text="浏览", command=self.browse_destination_dir)
        self.destination_button.pack()

        # 创建目标文件格式标签和输入框
        self.format_label = tk.Label(self.master, text="目标文件格式:")
        self.format_label.pack()
        self.format_entry = tk.Entry(self.master)
        self.format_entry.pack()

        # 创建选择拷贝方式的选择框
        self.copy_method_var = tk.StringVar()
        self.copy_method_var.set("overwrite")  # 设置默认值

        # 设置三个选项的单选按钮
        self.format_label = tk.Label(self.master, text="选择处理重名文件方式:")
        self.format_label.pack()
        self.overwrite_radio = tk.Radiobutton(self.master, text="覆盖已有文件", variable=self.copy_method_var,
                                              value="overwrite")
        self.overwrite_radio.pack()

        self.add_number_radio = tk.Radiobutton(self.master, text="添加数字后缀", variable=self.copy_method_var,
                                               value="add_number")
        self.add_number_radio.pack()

        self.add_parent_dir_radio = tk.Radiobutton(self.master, text="添加父目录名", variable=self.copy_method_var,
                                                   value="add_parent_dir")
        self.add_parent_dir_radio.pack()

        # 创建按钮框架，包含开始拷贝和清空日志按钮
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        # 创建开始拷贝按钮并放置在左侧
        self.start_button = tk.Button(button_frame, text="开始拷贝", command=self.start_copy)
        self.start_button.pack(side=tk.LEFT)

        # 创建按钮框架中的占位标签，用于在两个按钮之间创建空间
        spacer_label = tk.Label(button_frame, text="", width=1)
        spacer_label.pack(side=tk.LEFT)

        # 创建清空日志按钮并放置在右侧
        self.clear_button = tk.Button(button_frame, text="清空日志", command=self.clear_log)
        self.clear_button.pack(side=tk.RIGHT)

        # 创建日志文本框，用于显示日志信息
        self.log_text = tk.Text(self.master)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def browse_source_dir(self):
        # 通过文件对话框选择源文件夹路径，并将路径显示在输入框中
        source_dir = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, source_dir)

    def browse_destination_dir(self):
        # 通过文件对话框选择目标文件夹路径，并将路径显示在输入框中
        destination_dir = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, destination_dir)

    def start_copy(self):
        # 如果选择拷贝方式为父目录名，则弹出提示框
        if self.copy_method_var.get() == "add_parent_dir":
            self.master.bell()
            if not messagebox.askyesno("提示",
                                       "添加父目录后若出现重复会直接使用根目录作为文件名\n且若还有重名则直接覆盖\n这种方式可能导致文件名过长，是否继续？"):
                return
        # 清空日志文本框中的内容
        self.clear_log()
        # 从输入框中获取源文件夹路径、目标文件夹路径和目标文件格式
        # 创建拷贝配置参数对象，并调用文件操作类进行文件拷贝
        self.copyConfigParams = CopyConfigParams(
            self.source_entry.get(),
            self.destination_entry.get(),
            self.format_entry.get(),
            self.copy_method_var.get()
        )
        # 调用文件操作类的静态方法进行文件拷贝
        FileOperations.starter(self.copyConfigParams, self.log_message)

    def clear_log(self):
        # 清空日志文本框中的内容
        self.log_text.delete('1.0', tk.END)

    def log_message(self, message):
        # 将日志信息插入到日志文本框中
        self.log_text.insert(tk.END, message)

    def refresh_radio_buttons(self):
        # 根据self.copy_method_var的值设置单选按钮的选中状态
        if self.copy_method_var.get() == "overwrite":
            self.overwrite_radio.select()
        elif self.copy_method_var.get() == "add_number":
            self.add_number_radio.select()
        elif self.copy_method_var.get() == "add_parent_dir":
            self.add_parent_dir_radio.select()
