# coding=gbk
# 在Pycharm中设定该项目的编码为GBK，与cmd的编码方式一致，以消除cmd在控制台中输出的乱码。

import os

# 设定路径
print('\033[1;32m' + '开始运行：' + '\033[0m')
# 源目录
source_root = r'D:\OneDrive\CreativeSpace\PracticalArticle'
# 目标位置的目录
target_root = r'D:\GitHub\Local_PracticalArticle'

# 手动输入：待同步的源文件和文件夹的名称
# source_files = [
#     "Wei_Wang_Yang 1125.tex",
# ]
# source_folders = [
#     "Code",
# ]


# 自动获取：用排除法获取待同步的源文件和文件夹的名称
unsync_files = [
    '.aux',
    '.log',
    '.out',
    '.gz',
    '.gitignore',
    '.gitattributes',
]
unsync_folders = []

# 初始化
source_files = []
source_folders = []

# 如果目标目录不存在，就创建它
if not os.path.exists(target_root):
    os.makedirs(target_root)

# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
i = 0
for root, folders, files in os.walk(source_root):
    # 只在根目录下运作
    if root == source_root:
        # 获取所需文件的名称
        for file in files:
            for unsync_file in unsync_files:
                if unsync_file in file:
                    i = i + 1
            if i == 0:
                source_files.append(file)
            i = 0

        # 获取所需文件夹的名称
        for folder in folders:
            for unsync_folder in unsync_folders:
                if unsync_folder in folder:
                    i = i + 1
            if i == 0:
                source_folders.append(folder)
            i = 0
        # 结束
        print('\033[1;32m' + '获取文件和文件夹成功！' + '\033[0m')
        break

# 调用cmd执行mlink命令，为文件创建硬链接
print('\033[1;32m' + '正在创建文件链接' + '\033[0m')
i = 1
for source_file in source_files:
    print('\033[0;34m' + '对第' + str(i) + '个文件进行检查' + '\033[0m')

    source_path = os.path.join(source_root, source_file)
    target_path = os.path.join(target_root, source_file)
    cmd = 'MKLINK /h \"' + target_path + '\" \"' + source_path + '\"'
    print('执行： ' + cmd)
    os.system(cmd)

    i = i + 1

# 调用cmd执行mlink命令，为文件夹创建目录联接
print('\033[1;32m' + '正在创建文件夹链接' + '\033[0m')
i = 1
for source_folder in source_folders:
    print('\033[0;34m' + '对第' + str(i) + '个文件夹进行检查' + '\033[0m')

    source_path = os.path.join(source_root, source_folder)
    target_path = os.path.join(target_root, source_folder)
    cmd = 'MKLINK /j \"' + target_path + '\" \"' + source_path + '\"'
    print('执行命令： ' + cmd)
    os.system(cmd)

    i = i + 1

print('\033[1;32m' + '执行完毕！' + '\033[0m')
