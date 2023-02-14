# 操作json file的常用方法
import json


def Enca_json_load(filePath):
    '''
    json_load:读取json文件
    return: json数据格式
    '''
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return json.load(file)


def Enca_json_loads(data):
    '''
    json_loads:将字符串数据解析为python数据格式,字符串需要提前转换成双引号
    data： '["hello",{"username":"xiaoliu"}]'
    return: python数据类型
    '''
    return json.loads(data)


def Enca_json_dump(filePath, data):
    '''
    json_dump:写入json文件
    data： 写入的数据
    filePath:文件路径及文件 示例* ./123.json
    '''
    with open(filePath, mode='a', newline='', encoding='utf8', ) as file:
        json.dump(data, file, ensure_ascii=False)


def Enca_json_dumps(data):
    '''
    json_dumps:将数据转换成字符串
    data: [{'username':'zhangsan','sex':6},{'username':'lisi','sex':3}]
    return: 返回为当前数据的字符串类型
    '''
    return json.dumps(data)
