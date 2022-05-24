import os
import shutil

try:
    os.remove('./images_sort/ironman/截屏2022-05-19 下午8.50.19.png')
    os.remove('./images_sort/ironman/截屏2022-05-19 下午8.50.29.png')
    os.remove('./images_sort/ironman/截屏2022-05-19 下午8.50.47.png')
    os.remove('./images_sort/ironman/截屏2022-05-19 下午8.51.17.png')
    os.remove('./images_sort/spiderman1/截屏2022-05-19 下午8.45.43.png')
    os.remove('./images_sort/spiderman1/截屏2022-05-19 下午8.46.08.png')
    os.remove('./images_sort/spiderman1/截屏2022-05-19 下午8.46.31.png')
    os.remove('./images_sort/long/截屏2022-05-19 下午8.52.56.png')
    os.remove('./images_sort/long/截屏2022-05-19 下午8.52.46.png')
    os.remove('./images_sort/long/截屏2022-05-19 下午8.52.29.png')
    os.remove('./images_sort/spiderman2/截屏2022-05-19 下午8.48.22.png')
    os.remove('./images_sort/spiderman2/截屏2022-05-19 下午8.48.31.png')
    os.remove('./images_sort/spiderman2/截屏2022-05-19 下午8.48.54.png')
    os.remove('./images_sort/spiderman2/截屏2022-05-19 下午8.49.01.png')
except:
    try:
        shutil.rmtree('./auto_sort')
    except:
        pass



