import os
import datetime

class BackupUtility:
    def __init__(self, root_folder, output_folder, output_format):
        """
        初始化备份工具对象。

        Parameters:
        - root_folder (str): 根文件夹路径
        - output_folder (str): 输出文件夹路径
        - output_format (str): 输出格式（例如 'txt' 或 'md'）
        """
        self.root_folder = root_folder
        self.output_folder = output_folder
        self.output_format = output_format

    def backup_folder_structure(self):
        """
        备份文件夹目录结构。

        使用递归方法遍历目录树，将文件夹结构和文件信息写入输出文件中。

        Returns:
        - str: 输出文件的路径
        """
        # 获取当前时间作为备份文件名的一部分
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # 构建输出文件的路径
        output_file_path = os.path.join(
            self.output_folder, f"directory_structure_{current_time}.{self.output_format}"
        )
        # 打开输出文件，写入文件夹结构和文件信息
        with open(output_file_path, 'w') as output_file:
            for folder_name, subfolders, files in os.walk(self.root_folder):
                # 计算文件夹的深度，用于缩进显示
                depth = folder_name.count(os.sep) - self.root_folder.count(os.sep)
                indent = '    ' * depth
                # 写入文件夹信息到输出文件中
                output_file.write(f"{indent}|-- {os.path.basename(folder_name)}/\n")
                # 写入文件信息到输出文件中
                for file in files:
                    output_file.write(f"{indent}    |-- {file}\n")
        return output_file_path
