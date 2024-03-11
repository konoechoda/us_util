import os
import shutil


class FileOperations:
    @staticmethod
    def starter(settings, log_callback):
        """
        静态方法，用于复制文件

        参数:
        - settings: 包含复制操作所需参数的对象
        - log_callback: 用于记录日志的回调函数
        """
        # 判断settings对象是否为None
        if settings is None:
            log_callback("Error: Settings object is None.\n")
            return

        # 判断源文件夹路径是否为空
        if not settings.source_dir:
            log_callback("Error: Source directory is empty.\n")
            return

        # 判断目标文件夹路径是否为空
        if not settings.destination_dir:
            log_callback("Error: Destination directory is empty.\n")
            return

        # 判断文件格式是否为空
        if not settings.file_format:
            log_callback("Error: File format is empty.\n")
            return

        # 如果文件格式没有以点号开头，则添加点号
        if not settings.file_format.startswith('.'):
            settings.file_format = '.' + settings.file_format

        # 开始文件复制过程的日志记录
        log_callback("Starting file copy process...\n")

        # 根据用户选择的拷贝方式调用相应的静态方法
        if settings.copy_method == "overwrite":
            log_callback("Copy_method(if needed): Overwriting existing files...\n")
            FileOperations.copy_files(settings, log_callback)
        if settings.copy_method == "add_number":
            log_callback("Copy_method(if needed): Adding number suffix...\n")
            FileOperations.copy_files_with_number(settings, log_callback)
        elif settings.copy_method == "add_parent_dir":
            log_callback("Copy_method(if needed): Adding parent directory name...\n")
            FileOperations.copy_files_with_father(settings, log_callback)
        else:
            FileOperations.copy_files(settings, log_callback)

    @staticmethod
    def copy_files(settings, log_callback):
        # 初始化成功和错误计数器
        counter_success = 0
        counter_error = 0

        # 处理覆盖已有文件的拷贝方式
        # 遍历源文件夹
        for root, dirs, files in os.walk(settings.source_dir):
            for file in files:
                # 检查文件是否以指定格式结尾
                if file.endswith(settings.file_format):
                    # 构建源文件和目标文件的路径
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(settings.destination_dir, file)
                    try:
                        # 尝试复制文件
                        shutil.copy2(source_file, dest_file)
                        # 记录成功复制的文件
                        log_callback(f"Copying file: {file} to {dest_file}\n")
                        counter_success += 1
                    except Exception as e:
                        # 记录复制过程中的错误
                        log_callback(f"Error copying file {file}: {str(e)}\n")
                        counter_error += 1

        # 文件复制过程完成的日志记录
        log_callback(f"File copy process completed.\n {counter_success} files copied,\n {counter_error} errors.\n")

    @staticmethod
    def copy_files_with_number(settings, log_callback):
        # 初始化成功和错误计数器
        counter_success = 0
        counter_error = 0

        # 遍历源文件夹
        for root, dirs, files in os.walk(settings.source_dir):
            for file in files:
                # 检查文件是否以指定格式结尾
                if file.endswith(settings.file_format):
                    # 构建源文件和目标文件的路径
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(settings.destination_dir, file)
                    try:
                        # 如果目标文件已经存在，则添加数字后缀
                        if os.path.exists(dest_file):
                            file_name, file_extension = os.path.splitext(dest_file)
                            # 递增数字后缀直到找到一个可用的文件名
                            index = 1
                            while os.path.exists(f"{file_name}_{index}{file_extension}"):
                                index += 1
                            dest_file = f"{file_name}_{index}{file_extension}"
                        # 尝试复制文件
                        shutil.copy2(source_file, dest_file)
                        # 记录成功复制的文件
                        log_callback(f"Copying file: {file} to {dest_file}\n")
                        counter_success += 1
                    except Exception as e:
                        # 记录复制过程中的错误
                        log_callback(f"Error copying file {file}: {str(e)}\n")
                        counter_error += 1

        # 文件复制过程完成的日志记录
        log_callback(f"File copy process completed.\n {counter_success} files copied,\n {counter_error} errors.\n")

    @staticmethod
    def copy_files_with_father(settings, log_callback):
        """
        静态方法，用于复制文件

        参数:
        - settings: 包含复制操作所需参数的对象
        - log_callback: 用于记录日志的回调函数
        """
        # 初始化成功和错误计数器
        counter_success = 0
        counter_error = 0

        # 遍历源文件夹
        for root, dirs, files in os.walk(settings.source_dir):
            for file in files:
                # 检查文件是否以指定格式结尾
                if file.endswith(settings.file_format):
                    # 构建源文件和目标文件的路径
                    source_file = os.path.join(root, file)
                    # 构建目标文件的路径，初始化目标文件名为原始文件名
                    dest_file = os.path.join(settings.destination_dir, file)

                    # 如果目标文件已经存在，则进一步添加父目录的父目录名称
                    if os.path.exists(dest_file):
                        # 获取源文件的父目录名称
                        parent_folder_name = os.path.basename(os.path.abspath(os.path.join(source_file, os.pardir)))
                        # 更新目标文件的路径
                        dest_file = os.path.join(settings.destination_dir, f"{parent_folder_name}_{file}")

                    # 如果目标文件已经存在，则直接使用源文件完整路径作为目标文件路径
                    if os.path.exists(dest_file):
                        # 直接使用源文件完整路径作为目标文件路径
                        file_name = source_file.replace("/", "_").replace(":", "_").replace(os.path.sep, "_")
                        dest_file = os.path.join(settings.destination_dir, f"{file_name}")
                    try:
                        # 尝试复制文件
                        shutil.copy2(source_file, dest_file)
                        # 记录成功复制的文件
                        log_callback(f"Copying file: {file} to {dest_file}\n")
                        counter_success += 1
                    except Exception as e:
                        # 记录复制过程中的错误
                        log_callback(f"Error copying file {file}: {str(e)}\n")
                        counter_error += 1

        # 文件复制过程完成的日志记录
        log_callback(f"File copy process completed.\n {counter_success} files copied,\n {counter_error} errors.\n")
