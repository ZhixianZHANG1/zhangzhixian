import os

# 填写照片所在的目录路径
dir_path = r'C:\Users\73455\Videos\photo'

# 获取目录下所有文件名
file_list = os.listdir(dir_path)

# 将文件名按照数字大小排序
file_list.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

# 遍历文件列表，将文件分组放入不同的文件夹
for i, file_name in enumerate(file_list):
    # 每6个文件新建一个文件夹
    if i % 6 == 0:
        folder_name = file_name.split('_')[1].split('.')[0]
        folder_path = os.path.join(dir_path, folder_name)
        # 判断文件夹是否存在，不存在则新建
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    # 将文件移动到对应的文件夹中
    file_path = os.path.join(dir_path, file_name)
    new_file_path = os.path.join(folder_path, file_name)
    os.rename(file_path, new_file_path)

print('文件分类完成！')
