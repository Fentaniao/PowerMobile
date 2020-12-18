# coding=gbk
# ��Pycharm���趨����Ŀ�ı���ΪGBK����cmd�ı��뷽ʽһ�£�������cmd�ڿ���̨����������롣

import os

# �趨·��
print('\033[1;32m' + '��ʼ���У�' + '\033[0m')
# ԴĿ¼
source_root = r'D:\OneDrive\CreativeSpace\PracticalArticle'
# Ŀ��λ�õ�Ŀ¼
target_root = r'D:\GitHub\Local_PracticalArticle'

# �ֶ����룺��ͬ����Դ�ļ����ļ��е�����
# source_files = [
#     "Wei_Wang_Yang 1125.tex",
# ]
# source_folders = [
#     "Code",
# ]


# �Զ���ȡ�����ų�����ȡ��ͬ����Դ�ļ����ļ��е�����
unsync_files = [
    '.aux',
    '.log',
    '.out',
    '.gz',
    '.gitignore',
    '.gitattributes',
]
unsync_folders = []

# ��ʼ��
source_files = []
source_folders = []

# ���Ŀ��Ŀ¼�����ڣ��ʹ�����
if not os.path.exists(target_root):
    os.makedirs(target_root)

# root ��ָ���ǵ�ǰ���ڱ���������ļ��еı���ĵ�ַ
# dirs ��һ�� list�������Ǹ��ļ��������е�Ŀ¼������(��������Ŀ¼)
# files ͬ���� list, �����Ǹ��ļ��������е��ļ�(��������Ŀ¼)
i = 0
for root, folders, files in os.walk(source_root):
    # ֻ�ڸ�Ŀ¼������
    if root == source_root:
        # ��ȡ�����ļ�������
        for file in files:
            for unsync_file in unsync_files:
                if unsync_file in file:
                    i = i + 1
            if i == 0:
                source_files.append(file)
            i = 0

        # ��ȡ�����ļ��е�����
        for folder in folders:
            for unsync_folder in unsync_folders:
                if unsync_folder in folder:
                    i = i + 1
            if i == 0:
                source_folders.append(folder)
            i = 0
        # ����
        print('\033[1;32m' + '��ȡ�ļ����ļ��гɹ���' + '\033[0m')
        break

# ����cmdִ��mlink���Ϊ�ļ�����Ӳ����
print('\033[1;32m' + '���ڴ����ļ�����' + '\033[0m')
i = 1
for source_file in source_files:
    print('\033[0;34m' + '�Ե�' + str(i) + '���ļ����м��' + '\033[0m')

    source_path = os.path.join(source_root, source_file)
    target_path = os.path.join(target_root, source_file)
    cmd = 'MKLINK /h \"' + target_path + '\" \"' + source_path + '\"'
    print('ִ�У� ' + cmd)
    os.system(cmd)

    i = i + 1

# ����cmdִ��mlink���Ϊ�ļ��д���Ŀ¼����
print('\033[1;32m' + '���ڴ����ļ�������' + '\033[0m')
i = 1
for source_folder in source_folders:
    print('\033[0;34m' + '�Ե�' + str(i) + '���ļ��н��м��' + '\033[0m')

    source_path = os.path.join(source_root, source_folder)
    target_path = os.path.join(target_root, source_folder)
    cmd = 'MKLINK /j \"' + target_path + '\" \"' + source_path + '\"'
    print('ִ����� ' + cmd)
    os.system(cmd)

    i = i + 1

print('\033[1;32m' + 'ִ����ϣ�' + '\033[0m')
