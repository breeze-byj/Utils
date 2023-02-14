# 操作yaml file的常用方法

import yaml


class YamlFuncation:
    def __init__(self, file):
        self.file = file

    def Enca_read_yaml(self, encoding='utf-8'):
        """读取yaml数据"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def Enca_write_yaml(self, data, encoding='utf-8'):
        """向yaml文件写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


print(YamlFuncation('./config.yaml').Enca_read_yaml())
