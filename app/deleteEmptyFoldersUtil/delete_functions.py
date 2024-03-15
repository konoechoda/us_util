import os


def remove_empty_folders(root_folder, log_text):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                log_text.insert(tk.END, f"删除空文件夹：{folder_path}\n")
            else:
                remove_empty_folders(folder_path, log_text)
