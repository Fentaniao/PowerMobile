# ���ļ����µ��ļ�˫��ͬ��

import os
import shutil

# �趨·��
# EndNoteͼ�����ָ��·��������Ŀ¼����0_EndnoteArticle��һ��Ŀ¼��
print('\033[1;34m' + '���ڶ����趨��Ŀ¼����ͬ��' + '\033[0m')
source_path = os.path.abspath(r'D:\My Files\My EndNote Library.Data\PDF')
target_path = os.path.abspath(r'D:\OneDrive\Research\0_EndnoteArticle')

# ���Ŀ��Ŀ¼�����ڣ��ʹ�����
if not os.path.exists(target_path):
    os.makedirs(target_path)


# ��ȡ��Ŀ¼���ļ���
def get_sub_sub_root_name(root, sub_root):
    lindex = str(root).rfind(sub_root)
    rindex = lindex + len(sub_root)
    sub_sub_root = root[rindex:]
    return sub_sub_root


# ʹ��xcopy+cmd��������ͬ��
def inc_sync():
    if os.path.exists(source_path):
        # root ��ָ���ǵ�ǰ���ڱ���������ļ��еı���ĵ�ַ
        # dirs ��һ�� list�������Ǹ��ļ��������е�Ŀ¼������(��������Ŀ¼)
        # files ͬ���� list, �����Ǹ��ļ��������е��ļ�(��������Ŀ¼)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)

                # ����cmdִ��xcopy���������ֵresult
                # ��Pycharm���趨����Ŀ�ı���ΪGBK����cmd�ı��뷽ʽһ�£�������cmd�ڿ���̨����������롣
                cmd = 'xcopy \"' + src_file + '\" \"' + target_path + '\" /s /d /y'

                sub_root = '\\PDF\\'
                sub_sub_root = get_sub_sub_root_name(root, sub_root)
                print('\033[1;34m' + "����Ŀ¼ " + sub_sub_root + " ��", end='')
                result = os.system(cmd)

                # ������
                print('\033[0;30m' + '����' + str(file) + '\033[0m')


# ʹ�ü���ļ����Ƿ���ڵķ�ʽ����ɾ��
def del_sync():
    # ��source_filesװ��source_path�е��ļ���
    source_files = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            source_files.append(file)

    # ��target_filesװ��target_path�����е��ļ���
    target_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            target_files.append(file)

    # ���target_path�е��ļ��Ƿ���source_path�У���������ɾȥ
    for target_file in target_files:
        if target_file not in source_files:
            del_path = os.path.join(target_path, target_file)
            os.remove(del_path)

            print('\033[1;31m' + 'ɾ����' + str(del_path) + '\033[0m')


# ��source_path��target_path��ͬ��
print('\033[1;32m' + '��ʼ�����ļ�' + '\033[0m')
inc_sync()
print('\033[1;32m' + '�������' + '\033[0m')

# ��target_pathɾ�����в���source_path�е��ļ�
print('\033[1;31m' + '��ʼɾ���ļ�' + '\033[0m')
del_sync()
print('\033[1;31m' + 'ɾ�����' + '\033[0m')
