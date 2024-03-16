import os
import tkinter as tk
from tkinter import filedialog, messagebox
from app.deleteEmptyFoldersUtil.delete_functions import FolderCleaner
from app.deleteEmptyFoldersUtil.backup_functions import BackupUtility


class DeleteEmptyFoldersAppGUI:
    def __init__(self, master):
        # 初始化窗口
        self.window = master
        # 创建界面组件
        self.create_widgets()
        # 刷新单选按钮状态
        self.refresh_radio_buttons()

    def create_widgets(self):
        # 创建目标文件夹路径标签、输入框和浏览按钮
        self.lbl_target = tk.Label(self.window, text="目标文件夹路径:")
        self.lbl_target.pack()
        self.entry_target = tk.Entry(self.window, width=50)
        self.entry_target.pack()
        self.btn_browse_target = tk.Button(
            self.window, text="浏览", command=lambda: self.entry_target.insert(tk.END, filedialog.askdirectory())
        )
        self.btn_browse_target.pack()

        # 创建输出文件夹路径标签、输入框和浏览按钮
        self.lbl_output = tk.Label(self.window, text="备份文件输出路径:")
        self.lbl_output.pack()
        self.entry_output = tk.Entry(self.window, width=50)
        self.entry_output.pack()
        self.btn_browse_output = tk.Button(
            self.window, text="浏览", command=lambda: self.entry_output.insert(tk.END, filedialog.askdirectory())
        )
        self.btn_browse_output.pack()

        # 创建选择输出格式的标签和单选按钮
        self.lbl_format = tk.Label(self.window, text="选择备份文件输出格式:")
        self.lbl_format.pack()
        self.format_var = tk.StringVar()
        self.format_var.set("txt")
        self.format_txt = tk.Radiobutton(self.window, text="txt", variable=self.format_var, value="txt")
        self.format_txt.pack()
        self.format_md = tk.Radiobutton(self.window, text="md", variable=self.format_var, value="md")
        self.format_md.pack()

        # 创建执行备份和删除按钮
        self.btn_execute = tk.Button(self.window, text="执行备份和删除", command=self.backup_and_remove_empty_folders)
        self.btn_execute.pack()

        # 创建日志文本框
        self.log_text = tk.Text(self.window, height=10, width=80)
        self.log_text.pack()

    def backup_and_remove_empty_folders(self):
        # 获取目标文件夹路径、输出文件夹路径和输出格式
        target_directory = self.entry_target.get()
        output_directory = self.entry_output.get()
        output_format = self.format_var.get()

        # 检查目标路径和输出路径是否存在且为文件夹
        if os.path.isdir(target_directory) and os.path.isdir(output_directory):
            # 弹出确认对话框
            confirmed = messagebox.askyesno("确认操作",
                                            "确定要执行备份和删除操作吗？\n请注意：备份仅输出文件夹目录结构。删除操作不可逆！")
            if confirmed:
                # 清空日志文本框
                self.log_text.delete(1.0, tk.END)
                # 执行备份操作并获取文件夹目录结构输出路径
                backup_utility = BackupUtility(target_directory, output_directory, output_format)
                directory_structure_path = backup_utility.backup_folder_structure()
                # 在日志文本框中显示备份结果和删除空文件夹的操作
                self.log_text.insert(tk.END, f"文件夹目录结构已输出到：{directory_structure_path}\n")
                FolderCleaner(target_directory, self.log_text).remove_empty_folders()
                self.log_text.insert(tk.END, "空文件夹删除完成！\n")
        else:
            self.log_text.insert(tk.END, "目标路径或输出路径不存在或不是文件夹。\n")

    def refresh_radio_buttons(self):
        # 根据当前的输出格式值刷新单选按钮状态
        if self.format_var.get() == "txt":
            self.format_txt.select()
        elif self.format_var.get() == "md":
            self.format_md.select()

    def run(self):
        # 运行主界面
        self.window.mainloop()
