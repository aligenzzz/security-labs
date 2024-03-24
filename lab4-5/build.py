# FOR GET .EXE
# python build.py main.py

import os
import sys
from PyInstaller.__main__ import run

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
USERS_PATH = os.path.join(current_dir_path, 'users.json')

if __name__ == '__main__':
    sys.argv += ['--onefile', '--add-data', f'{USERS_PATH};.']
    run()