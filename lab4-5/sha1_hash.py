import hashlib
import os

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as file:
        hasher = hashlib.sha1()
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
        return hasher.hexdigest()

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)

exe_path = os.path.join(current_dir_path, 'dist', 'main.exe')
hash_path = os.path.join(current_dir_path, 'dist', 'expected_sha1.txt')

hash_value = calculate_file_hash(exe_path)

with open(hash_path, 'w') as file:
    file.write(hash_value)