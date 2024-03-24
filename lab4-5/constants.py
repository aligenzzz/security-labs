import os

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)

USERS_PATH = os.path.join(current_dir_path, 'users.json')
API_KEY = '49f67d33a63f76775269d2cfd50e0858'