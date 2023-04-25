# 其他文件处理方法
import win32file as w
import os


# 判断文件资源是否被占用
def Enca_is_open(filename):
    if not os.access(filename, os.F_OK):
        return False
    try:
        handle = w.CreateFile(filename, w.GENERIC_WRITE, 0, None, w.OPEN_EXISTING, w.FILE_ATTRIBUTE_NORMAL, None)
        if int(handle) == w.INVALID_HANDLE_VALUE:
            return True
        w.CloseHandle(handle)
    except Exception:
        return True
    return False


# 获取文件夹下的所有文件,以list返回
def Enca_get_file_list(folder_name):
    return os.listdir(folder_name)


# 删除文件
def Enca_delete_file(file_name):
    os.remove(file_name)


# 读取当前文件绝对路径
def Enca_get_file_absolute_path():
    return os.path.abspath(__file__)


# 读取当前文件所在目录
def Enca_get_file_dirname():
    return os.path.dirname(os.path.abspath(__file__))  # 上级目录


# 获取当前文件所在目录的上一级目录
def Enca_get_file_absolute_dirname():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 上级目录


# 获取指定文件的路径
def Enca_get_this_file_path(file_name):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.abspath(cur_dir + os.path.sep + ".."), file_name)


# 若不存在***文件夹，则自动创建
def Enca_ismkdir(file_path):
    if not os.path.exists(file_path): os.mkdir(file_path)
   
# 图片下载
def download_img(url, num):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        # 将内容写入图片
        open(f'./{num}.jpg', 'wb').write(r.content)
    del r