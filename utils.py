import os
import shutil

def set_folder(folder_path, rewrite=False):
    if os.path.exists(folder_path) and rewrite:
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)