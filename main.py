import os

# 填写照片所在的目录路径
dir_path = r'C:\Users\73455\Videos\photo'
file_list = os.listdir(dir_path)



file_list.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))


folder_num = 1  # 初始文件夹编号为1



for i, file_name in enumerate(file_list):


    if i % 4 == 0:
        folder_name = str(folder_num)
        folder_path = os.path.join(dir_path, folder_name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        folder_num += 1  


    file_path = os.path.join(dir_path, file_name)
    new_file_path = os.path.join(folder_path, file_name)
    os.rename(file_path, new_file_path)


print('文件分类完成！')
