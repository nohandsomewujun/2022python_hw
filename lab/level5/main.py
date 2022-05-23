import face_recognition
import os
import shutil  # copy file


def read_known_face_path(dir):
    res = []
    res1 = []
    # 读取./images_sort下所有子文件夹的目录
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in dirs:
            res.append(os.path.join(root, name))
        for name in files:
            res1.append(os.path.join(root, name))
    return res, res1


# 读取将要分类保存的子文件夹路径和读取的face的文件路径
save_dir = './images_sort'
save_path, known_face_path = read_known_face_path(save_dir)

# 将各个子文件夹的已知face读入
known_face_encoding = []
for known_face in known_face_path:
    im = face_recognition.load_image_file(known_face)
    im_encoding = face_recognition.face_encodings(im)[0]
    known_face_encoding.append(im_encoding)


read_dir = './images'
read_face_list = []
for root, dirs, files in os.walk(read_dir, topdown=False):
    for name in files:
        read_face_list.append(os.path.join(root, name))

# 读入未知图片
for face in read_face_list:
    unknown_face_image = face_recognition.load_image_file(face)
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_face_image)[
            0]
    except IndexError:
        # 照片中没有face的时候
        continue
    results = face_recognition.compare_faces(
        known_face_encoding, unknown_face_encoding)
    for i in range(len(results)):
        if results[i] == 1:
            shutil.copy(face, save_path[i])
