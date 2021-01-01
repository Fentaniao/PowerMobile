# coding=gbk
import os

# 所有需要维护的md文件的路径
md_files_path = [
    "D:\OneDrive\Folder\Personal\个人简历.md",

]

md_error_file_path = []

# 文件校验
for md_file_path in md_files_path:
    if os.path.isfile(md_file_path):
        r_dot_index = md_file_path.rfind('.')
        if md_file_path[r_dot_index:] == ".md":
            print(md_file_path + ' is right.')
        else:
            print(md_file_path + ' is error.')
            md_error_file_path.append(md_file_path)
            md_files_path.remove(md_file_path)

# 将正确的md文件批量转换为docx格式
for md_file_path in md_files_path:
    r_dot_index = md_file_path.rfind('.')
    docx_name = md_file_path[0: r_dot_index] + ".docx"
    cmd = "pandoc " + md_file_path + " -o " + docx_name
    result = os.system(cmd)
