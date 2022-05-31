import os
import shutil
from psutil import process_iter
from datetime import datetime


def set_folder(folder_path, rewrite=False):
    if os.path.exists(folder_path) and rewrite:
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


def check_port(port):
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                return True
    return False


def time_now(formato='%H:%M:%S'):
    return datetime.now().strftime(formato)
