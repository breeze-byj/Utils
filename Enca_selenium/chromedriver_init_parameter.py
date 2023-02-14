from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# 自定义浏览器启动参数
options = Options()

driver_path = (r'xx/chromedriver.exe')  # 指定驱动位置
options.add_argument('--user-data-dir=C:\Users\18036\AppData\Local\Google\Chrome\User Data')  # 设置成用户自己的数据目录,绝对路径
options.add_argument('user-agent=Mozilla/5.....')  # 伪装浏览器
options.add_argument('headless')  # 浏览器隐式启动
options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码
options.add_argument('disable-infobars')  # 隐藏自动化操作提示
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置开发者模式
options.add_argument('--disable-infobars')  # 禁止策略化
options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--incognito')  # 隐身模式（无痕模式）
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置，绝对路径
#指定selenium工具操作Chrome浏览器时下载文件的路径
prefs1 = {"download.default_directory":"D:\download"}
# prefs2 = {'profile.default_content_settings.popups': 0, 'download.default_directory': '默认下载路径'}  # 设置下载文件存放路径，这里要写绝对路径
options.add_experimental_option('prefs', prefs1)
# 禁止图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)


driver = Chrome(executable_path=driver_path,options=options)









