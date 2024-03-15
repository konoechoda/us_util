import os
import datetime


def backup_folder_structure(root_folder, output_folder, output_format):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_path = os.path.join(output_folder, f"directory_structure_{current_time}.{output_format}")
    with open(output_file_path, 'w') as output_file:
        for folder_name, subfolders, files in os.walk(root_folder):
            depth = folder_name.count(os.sep) - root_folder.count(os.sep)
            indent = '    ' * depth
            output_file.write(f"{indent}|-- {os.path.basename(folder_name)}/\n")
            for file in files:
                output_file.write(f"{indent}    |-- {file}\n")
    return output_file_path
