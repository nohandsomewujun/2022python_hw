from importlib.metadata import files
import face_recognition
import os

def read_known_face_path(dir):
    res = []
    # 读取./images_sort下所有子文件夹的目录
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in dirs:
            res.append(os.path.join(root, name))
    return res

