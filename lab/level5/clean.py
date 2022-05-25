import os


def cleantest(rm_dir):
    # 将rm_dir文件夹中的所有一级目录里的图片删除至一张
    # 便于测试前面的功能，不必反复手动删除

    # 得到一级目录
    f_dir = []
    for root, dirs, files in os.walk(rm_dir, topdown=False):
        for name in dirs:
            f_dir.append(os.path.join(root, name))

    for dir in f_dir:
        files = os.listdir(dir)
        if len(files) >= 2:
            for i in range(1, len(files)):
                os.remove(os.path.join(dir, files[i]))
