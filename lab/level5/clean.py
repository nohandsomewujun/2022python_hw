import os
import shutil

try:
    os.remove('./images_sort/ironman/3.2.png')
    os.remove('./images_sort/ironman/3.3.png')
    os.remove('./images_sort/ironman/3.4.png')
    os.remove('./images_sort/spiderman1/1.2.png')
    os.remove('./images_sort/spiderman1/1.4.png')
    os.remove('./images_sort/spiderman1/1.3.png')
    os.remove('./images_sort/spiderman1/1.1.png')
    os.remove('./images_sort/long/4.1.png')
    os.remove('./images_sort/long/4.2.png')
    os.remove('./images_sort/long/4.3.png')
    os.remove('./images_sort/long/4.4.png')
    os.remove('./images_sort/spiderman2/2.1.png')
    os.remove('./images_sort/spiderman2/2.2.png')
    os.remove('./images_sort/spiderman2/2.3.png')
    os.remove('./images_sort/spiderman2/2.4.png')
    os.remove('./images_sort/spiderman2/2.5.png')
except:
    try:
        shutil.rmtree('./auto_sort')
    except:
        pass



