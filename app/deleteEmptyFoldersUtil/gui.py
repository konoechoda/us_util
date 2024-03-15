import os
import tkinter as tk
from tkinter import filedialog, messagebox
from delete_functions import remove_empty_folders
from backup_functions import backup_folder_structure


def backup_and_remove_empty_folders():
    target_directory = entry_target.get()
    output_directory = entry_output.get()
    output_format = format_var.get()

    if os.path.isdir(target_directory) and os.path.isdir(output_directory):
        confirmed = messagebox.askyesno("确认操作", "确定要执行备份和删除操作吗？\n请注意：备份仅输出文件夹目录结构。删除操作不可逆！")
        if confirmed:
            log_text.delete(1.0, tk.END)
            directory_structure_path = backup_folder_structure(target_directory, output_directory, output_format)
            log_text.insert(tk.END, f"文件夹目录结构已输出到：{directory_structure_path}\n")
            remove_empty_folders(target_directory, log_text)
            log_text.insert(tk.END, "空文件夹删除完成！\n")
    else:
        log_text.insert(tk.END, "目标路径或输出路径不存在或不是文件夹。\n")


# 创建主窗口
window = tk.Tk()
window.title("选择输出格式")

# 添加目标文件夹路径输入框和按钮
lbl_target = tk.Label(window, text="目标文件夹路径:")
lbl_target.pack()
entry_target = tk.Entry(window, width=50)
entry_target.pack()
btn_browse_target = tk.Button(window, text="浏览",
                              command=lambda: entry_target.insert(tk.END, filedialog.askdirectory()))
btn_browse_target.pack()

# 添加输出文件夹路径输入框和按钮
lbl_output = tk.Label(window, text="输出文件夹路径:")
lbl_output.pack()
entry_output = tk.Entry(window, width=50)
entry_output.pack()
btn_browse_output = tk.Button(window, text="浏览",
                              command=lambda: entry_output.insert(tk.END, filedialog.askdirectory()))
btn_browse_output.pack()

# 添加输出格式选择
lbl_format = tk.Label(window, text="选择输出格式:")
lbl_format.pack()
format_var = tk.StringVar()
format_var.set("txt")  # 默认选择txt格式
format_txt = tk.Radiobutton(window, text="txt", variable=format_var, value="txt")
format_txt.pack()
format_md = tk.Radiobutton(window, text="md", variable=format_var, value="md")
format_md.pack()

# 添加执行按钮
btn_execute = tk.Button(window, text="执行备份和删除", command=backup_and_remove_empty_folders)
btn_execute.pack()

# 添加日志框
log_text = tk.Text(window, height=10, width=80)
log_text.pack()

# 启动主循环
window.mainloop()
