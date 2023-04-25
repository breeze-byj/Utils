import csv
import os
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from tqdm import tqdm


db = pymysql.connect(host='localhost', user='root', password='******', port=3306, db='db_name', charset='utf8')
cursor = db.cursor()
file = open("file_path", encoding='utf-8')
reader = csv.reader(file)
for item in reader:
    # 第一行是字段名跳过
    if (reader.line_num == 1):
        continue

    sql = 'INSERT INTO `表名` VALUES("%s","%s","%s","%s","%s","%s","%s")' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    try:
        cursor.execute(sql)
        db.commit()
        print("success:", reader.line_num)
    except Exception as ex:
        print("error:", reader.line_num)
        print("出现如下异常%s" % ex)
        db.rollback()
        break