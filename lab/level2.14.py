# level2.14 code
import easyocr
import os

dic_path = "./images/"
save_path = "./images_res/"
# 计算该目录下所有图片
# 实现自动化操作
image_namelist = os.listdir(dic_path)
print("计算" + " ".join(image_namelist))

# this needs to run only once to load the model into memory
# 本人穷，无gpu
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
i = 1

for image in image_namelist:
    s1 = dic_path + image
    print("开始计算:" + image)
    # 使用model来计算结果
    result = reader.readtext(s1, detail=0)
    # 将结果写入存放结果的目录
    s2 = save_path + image + '.txt'
    with open(s2, "w") as f:
        res = " ".join(result)
        f.write(res)
    print("第" + str(i) + "个计算完成." + "(" + image + ")")
    i = i + 1

print('All Done!')
