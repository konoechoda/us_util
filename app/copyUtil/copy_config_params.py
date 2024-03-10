class CopyConfigParams:
    def __init__(self, source_dir, destination_dir, file_format, copy_method):
        """
        初始化函数，用于创建拷贝配置参数对象

        参数:
        - source_dir: 源文件夹路径
        - destination_dir: 目标文件夹路径
        - file_format: 目标文件格式
        """
        # 设置源文件夹路径
        self.source_dir = source_dir
        # 设置目标文件夹路径
        self.destination_dir = destination_dir
        # 设置目标文件格式
        self.file_format = file_format
        # 设置拷贝方式
        self.copy_method = copy_method
