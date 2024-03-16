import os

class FolderCleaner:
    def __init__(self, root_folder, log_text):
        """
        初始化文件夹清理器对象。

        Parameters:
        - root_folder (str): 根文件夹路径
        - log_text (tk.Text): 日志文本框对象
        """
        self.root_folder = root_folder
        self.log_text = log_text

    def remove_empty_folders(self):
        """
        递归地删除空文件夹。

        使用递归方法遍历目录树，找到并删除所有空文件夹。

        Note:
        - 如果文件夹非空，则继续递归调用 `remove_empty_folders` 方法。
        - 如果文件夹为空，则删除该文件夹，并在日志文本框中显示删除信息。
        """
        for folder_name in os.listdir(self.root_folder):
            folder_path = os.path.join(self.root_folder, folder_name)
            if os.path.isdir(folder_path):
                if not os.listdir(folder_path):
                    # 如果文件夹为空，删除文件夹并记录日志
                    os.rmdir(folder_path)
                    self.log_text.insert(tk.END, f"删除空文件夹：{folder_path}\n")
                else:
                    # 如果文件夹非空，递归调用 remove_empty_folders 方法
                    FolderCleaner(folder_path, self.log_text).remove_empty_folders()
