# 操作ini file的常用方法
import configparser
import os


class InitializationFile:
    def __init__(self, filepath):
        self._path = filepath
        self.config = configparser.ConfigParser()  # 实例化解析对象
        parent_dir = os.path.dirname(os.path.abspath(__file__))  # 获取文件绝对路径
        self.config.read(parent_dir + filepath, encoding='utf-8')  # 读文件

    def Enca_get_sections(self):
        """
        获取ini文件所有的块，返回为list
        """
        sect = self.config.sections()
        return sect

    def Enca_get_options(self, sec):
        """
        获取ini文件指定块的项
        :param sec: 传入的块名
        :return: 返回指定块的项（列表形式）
        """
        return self.config.options(sec)

    def Enca_get_items(self, sec):
        """
        获取指定section的所有键值对
        :param sec: 传入的块名
        :return: section的所有键值对（元组形式）
        """
        return self.config.items(sec)

    def Enca_get_option(self, sec, opt):
        """
        :param sec: 传入的块名
        :param opt: 传入项
        :return: 返回项的值(string类型)
        """
        return self.config.get(sec, opt)

    def Enca_write(self):
        """ 将修改后写入文件 """
        with open(self._path, 'w') as fp:
            self.config.write(fp)

    def Enca_add_section(self, sec):
        """
        为ini文件添加新的section, 如果section 已经存在则抛出异常
        :param sec: 传入的块名
        :return: None
        """
        self.config.add_section(sec)
        self.Enca_write()

    def Enca_set_option(self, sec, opt, value):
        """
        对指定section下的某个option赋值
        :param sec: 传入的块名
        :param opt: 传入的项名
        :param value: 传入的值
        :return:  None
        """
        self.config.set(sec, opt, value)
        self.Enca_write()  # 写入文件

    def Enca_remove_sec(self, sec):
        """
        删除某个section
        :param sec: 传入的块名
        :return: bool
        """
        self.config.remove_section(sec)
        self.Enca_write()  # 写入文件

    def Enca_remove_opt(self, sec, opt):
        """
        删除某个section下的某个option
        :param sec: 传入的块名
        :param opt: 传入的项名
        :return: bool
        """
        self.config.remove_option(sec, opt)
        self.Enca_write()  # 写入文件


if __name__ == '__main__':
    # 加载文件, 初始化
    dis = InitializationFile('./replace.ini')

    # 获取ini文件所有的section
    print(dis.Enca_get_sections())

    # 获取指定section的所有options
    print(dis.Enca_get_options('trial_info'))

    # 获取指定section的所有键值对
    print(dis.Enca_get_items('trial_info'))

    # 获取指定section指定option的值
    print(dis.Enca_get_option('trial_info', 'scope'))

    # 对指定option赋值
    dis.Enca_set_option('trial_info', 'scope', '88')

    # 删除指定section
    dis.Enca_remove_sec('trial_info')

    # 增加section
    dis.Enca_add_section('trial_info')

    # 删除指定option
    dis.Enca_remove_opt('trial_info', 'scope')
