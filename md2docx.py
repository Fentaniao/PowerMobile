# coding=gbk
import os

# ������Ҫά����md�ļ���·��
md_files_path = [
    "D:\OneDrive\Folder\Personal\���˼���.md",

]

md_error_file_path = []

# �ļ�У��
for md_file_path in md_files_path:
    if os.path.isfile(md_file_path):
        r_dot_index = md_file_path.rfind('.')
        if md_file_path[r_dot_index:] == ".md":
            print(md_file_path + ' is right.')
        else:
            print(md_file_path + ' is error.')
            md_error_file_path.append(md_file_path)
            md_files_path.remove(md_file_path)

# ����ȷ��md�ļ�����ת��Ϊdocx��ʽ
for md_file_path in md_files_path:
    r_dot_index = md_file_path.rfind('.')
    docx_name = md_file_path[0: r_dot_index] + ".docx"
    cmd = "pandoc " + md_file_path + " -o " + docx_name
    result = os.system(cmd)
