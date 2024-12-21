import os
import shutil


def generateFile(path, text):
    dir_path, file_name = os.path.split(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

def copyFile(oldPath,newPath):
    dir_path, file_name = os.path.split(newPath)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    shutil.copy(oldPath, newPath)