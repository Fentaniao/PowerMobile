# 将文件夹下的文件双向同步

import os
import shutil

# 设定路径
# EndNote图书馆中指定路径有两级目录，而0_EndnoteArticle仅一级目录。
print('\033[1;34m' + '正在对所设定的目录进行同步' + '\033[0m')
source_path = os.path.abspath(r'D:\My Files\My EndNote Library.Data\PDF')
target_path = os.path.abspath(r'D:\OneDrive\Research\0_EndnoteArticle')

# 如果目标目录不存在，就创建它
if not os.path.exists(target_path):
    os.makedirs(target_path)


# 获取子目录的文件名
def get_sub_sub_root_name(root, sub_root):
    lindex = str(root).rfind(sub_root)
    rindex = lindex + len(sub_root)
    sub_sub_root = root[rindex:]
    return sub_sub_root


# 使用xcopy+cmd进行增量同步
def inc_sync():
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)

                # 调用cmd执行xcopy命令，并返回值result
                # 在Pycharm中设定该项目的编码为GBK，与cmd的编码方式一致，以消除cmd在控制台中输出的乱码。
                cmd = 'xcopy \"' + src_file + '\" \"' + target_path + '\" /s /d /y'

                sub_root = '\\PDF\\'
                sub_sub_root = get_sub_sub_root_name(root, sub_root)
                print('\033[1;34m' + "在子目录 " + sub_sub_root + " 中", end='')
                result = os.system(cmd)

                # 输出结果
                print('\033[0;30m' + '处理：' + str(file) + '\033[0m')


# 使用检查文件名是否存在的方式进行删除
def del_sync():
    # 用source_files装载source_path中的文件名
    source_files = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            source_files.append(file)

    # 用target_files装载target_path中所有的文件名
    target_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            target_files.append(file)

    # 检查target_path中的文件是否在source_path中，若不在则删去
    for target_file in target_files:
        if target_file not in source_files:
            del_path = os.path.join(target_path, target_file)
            os.remove(del_path)

            print('\033[1;31m' + '删除：' + str(del_path) + '\033[0m')


# 从source_path到target_path的同步
print('\033[1;32m' + '开始更新文件' + '\033[0m')
inc_sync()
print('\033[1;32m' + '更新完毕' + '\033[0m')

# 从target_path删除所有不在source_path中的文件
print('\033[1;31m' + '开始删除文件' + '\033[0m')
del_sync()
print('\033[1;31m' + '删除完毕' + '\033[0m')
