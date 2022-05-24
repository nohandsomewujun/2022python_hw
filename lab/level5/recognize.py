from ast import expr_context
import face_recognition
import os
import shutil  # copy file
from random import sample


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


def sort_by_known(save_dir, read_dir):
    # 读取将要分类保存的子文件夹路径和读取的face的文件路径
    save_path, known_face_path = read_known_face_path(save_dir)

    # 将各个子文件夹的已知face读入
    known_face_encoding = []
    for known_face in known_face_path:
        im = face_recognition.load_image_file(known_face)
        im_encoding = face_recognition.face_encodings(im)[0]
        known_face_encoding.append(im_encoding)

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


def auto_sort(save_dir, read_dir):
    # 将read_dir里面的所有照片分类归档到save_dir中
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # 创建一个默认的文件夹，用来放置无人脸的照片
    if not os.path.exists(os.path.join(save_dir, 'noface')):
        os.mkdir(os.path.join(save_dir, 'noface'))

    read_face_list = os.listdir(read_dir)
    for i in range(len(read_face_list)):
        read_face_list[i] = os.path.join(read_dir, read_face_list[i])

    # 创建字典，key对应图片路径，value对应其encoding
    unknown_face_encoding = {}
    for face in read_face_list:
        unknown_face_img = face_recognition.load_image_file(face)
        try:
            unknown_face_encoding[face] = face_recognition.face_encodings(unknown_face_img)[
                0]
        except IndexError:
            # 没有face的时候需要放入一个默认文件夹
            # 这里我们用对应key的value为0进行标记
            unknown_face_encoding[face] = 0

    # 使用集合列表来将分类好的face名放入集合
    no_face = set()
    sort_face = [set()]
    for key, value in unknown_face_encoding.items():

        isput = False

        if isinstance(value, int):
            no_face.add(key)
            continue

        for s in sort_face:
            if len(s) == 0:
                s.add(key)
                isput = True
                break
            else:
                one = sample(s, 1)[0]
                result = face_recognition.compare_faces(
                    [unknown_face_encoding[one]], value
                )
                if result[0] == 1:
                    s.add(key)
                    isput = True
                    break

        if isput == False:
            tmp = set()
            tmp.add(key)
            sort_face.append(tmp)

    # 将文件放入noface
    for img in no_face:
        shutil.copy(img, os.path.join(save_dir, 'noface'))
    # 将文件放入其他人脸文件夹
    i = 0
    for s in sort_face:
        if not os.path.exists(os.path.join(save_dir, 'face{}'.format(i))):
            os.mkdir(os.path.join(save_dir, 'face{}'.format(i)))
        for img in s:
            shutil.copy(img, os.path.join(save_dir, 'face{}'.format(i)))
        i = i + 1
