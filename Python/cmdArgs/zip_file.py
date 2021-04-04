import sys
import shutil
import os

if __name__ == '__main__':
    args_list = list(sys.argv)
    file_name = args_list[1]
    path = args_list[2]
    format_path = os.getcwd()+"\\"+path
    shutil.make_archive(file_name, 'zip', format_path)
