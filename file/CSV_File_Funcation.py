import glob
import os
import pandas as pd
import csv


# 操作csv file的常用方法

# 写入在csv文件第一行插入数据
def Enca_first_writh(csv_name, list):
    if os.access(csv_name, os.F_OK):
        df = pd.read_csv(csv_name, header=None, names=list)
        df.to_csv(csv_name, index=False)


# csv合并
def Enca_csv_merge(path, save_file_path):
    csv_list = glob.glob(path)
    print(u'共发现%s个CSV文件' % len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i, 'r').read()
        with open(save_file_path, 'a') as f:
            f.write(fr)
    print('合并完毕！')


# csv去重
def Enca_csv_deduplication(file_name):
    df = pd.read_csv(file_name, header=0, encoding='utf-8')
    datalist = df.drop_duplicates()
    datalist.to_csv(file_name, encoding='utf-8', header=None, index=None)
    print(f'{file_name}完成去重')


# 写入csv 追加
def Enca_write_csv(file_name, data_list_name):
    with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list_name:
            writer.writerow(row)


def Enca_csv_lod(filePath):
    '''
    csv_lod:读取文件
    return: [["line1","data1"],["line2","data2"]]
    '''
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return list(csv.reader(file))


def Enca_csv_dict_lod(filePath):
    '''
    csv_dict_lod:以字典的格式读取csv
    filePath:文件路径及文件 示例* ./123.csv
    return:[{"head1":"zhangsan","head2":"lisi","head3":"wangwu"}]
    '''
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return list(csv.DictReader(filter))


def Enca_csv_write(filePath, data):
    '''
    csv_writes:写入单行数据
    filePath:文件路径及文件 示例* ./123.csv
    data:写入该文件的数据 示例* ['data1','data2']
    '''
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


def Enca_csv_writes(filePath, data):
    '''
    csv_writes:写入多行数据
    filePath:文件路径及文件 示例* ./123.csv
    data:写入该文件的数据 示例* [('data1','data2'),('data3','data4')]
    '''
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        fw = csv.writer(file)
        fw.writerows(data)
    pass


def Enca_csv_dict_write(filePath, file_head, data):
    '''
    csv_dict_write:写入单行数据
    filePath:文件路径及文件 示例* ./123.csv
    file_head:写入的表头 示例* ['head1','head2','head3']
    data:写入该文件的数据 示例* {"head1":"zhangsan","head2":"lisi","head3":"wangwu"}
    '''
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        csv_dict = csv.DictWriter(file, fieldnames=file_head)
        csv_dict.writeheader()  # 写入表头
        csv_dict.writerow(data)  # 写入数据


def Enca_csv_dict_write_list(filePath, file_head, data):
    '''
    csv_dict_writes:写入多行数据
    filePath:文件路径及文件 示例* ./123.csv
    file_head:写入的表头 示例* ['head1','head2','head3']
    data:写入该文件的数据 示例* [{"head1":"zhangsan","head2":"lisi","head3":"wangwu"}]
    '''
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        csv_dict = csv.DictWriter(file, fieldnames=file_head)
        csv_dict.writeheader()  # 写入表头
        csv_dict.writerows(data)  # 写入数据
