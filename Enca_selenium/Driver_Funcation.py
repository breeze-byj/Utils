import time, pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException

# 对webdriver进行封装,用于模拟浏览器操作
class DriverFuncation:
    def __init__(self, drivertype='Chrome'):
        '''
        初始化浏览器
        :param drivertype:打开的浏览器类型
        '''
        if drivertype == 'Chrome':
            self.driver = webdriver.Chrome()
        if drivertype == 'FireFox':
            self.driver = webdriver.Firefox()
        if drivertype == 'Edge':
            self.driver = webdriver.Edge()

    def Enca_get_browser_name(self):
        '''
        获取浏览器名字
        :return:
        '''
        return self.driver.name

    def Enca_get_title(self):
        '''
        获取页面title
        :return:
        '''
        return self.driver.title

    def Enca_page_source(self):
        '''
        获取整个页面元素
        :return:
        '''
        return self.driver.page_source
    def find(self, element):
    '''
    元素选中效果
    '''
    STYLE = "background: green; border: 2px solid red;"
    self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, STYLE)
    return element

    def Enca_current_url(self):
        '''
        获取当前URL
        :return:
        '''
        return self.driver.current_url

    def Enca_visit_url(self, url):
        '''访问URL
        :param url: 需要访问的url
        :return:
        '''
        self.driver.get(url)

    def Enca_back(self):
        '''
        浏览器后退
        :return:
        '''
        self.driver.back()

    def Enca_forward(self):
        '''
        浏览器前进
        :return:
        '''
        self.driver.forward()

    def Enca_refresh(self):
        '''
        刷新
        :return:
        '''
        self.driver.refresh()

    def Enca_maximize_window(self):
        '''
        浏览器最大化
        :return:
        '''
        self.driver.maximize_window()

    def Enca_set_window_size(self, width, height):
        '''
        设置浏览器窗口大小
        :param width: 浏览器左右宽度
        :param height: 浏览器上下高度
        :return:
        '''
        self.driver.set_window_size(width, height)

    def Enca_get_window_position(self):
        '''
        获取当前浏览器窗口坐标
        :return:
        '''
        return self.driver.get_window_position()

    def Enca_switch_to_window(self, index):
        '''
        切换浏览器窗口
        :param index: -1 切换到新窗口,-2 切换到倒数第二个打开的窗口,0 切换到最开始打开的窗口
        :return:
        '''
        hand = self.driver.window_handles
        self.driver.switch_to.window(hand[index])

    def Enca_switch_to_default_content(self):
        '''
        返回最外层表单
        :return:
        '''
        return self.driver.switch_to.default_content()

    def Enca_switch_to_frame(self, frame_reference):
        '''
        切换至指定frame框架中
        :param frame_reference: iframe_name
        :return:
        '''
        self.driver.switch_to.frame(frame_reference)

    def Enca_switch_to_alert(self, type, send_keys=''):
        '''
        鼠标焦点切换到浏览器中的弹窗
        :param type: 操作类型；text（获取警告文本），accept（确认），dismiss（取消），send_keys(输入)
        :param send_keys: 操作类型为send_keys时输入的参数
        :return:
        '''
        if type == 'text':
            return self.driver.switch_to.alert.text()
        elif type == 'accept':
            self.driver.switch_to.alert.accept()
        elif type == 'dismiss':
            self.driver.switch_to.alert.dismiss()
        elif type == 'send_keys':
            self.driver.switch_to.alert.send_keys(send_keys)

    def Enca_delete_all_cookies(self):
        '''
        删除浏览器所有cookies
        :return:
        '''
        self.driver.delete_all_cookies()

    def Enca_delete_cookie(self, cookie_name):
        '''
        删除指定cookie
        :param cookie_name: 需要删除的cookie name
        :return:
        '''
        self.driver.delete_cookie(cookie_name)

    def Enca_get_cookes(self):
        '''
        返回当前cookie
        :return:
        '''
        return self.driver.get_cookies()

    def Enca_get_cookie(self, cookie_name):
        '''
        根据cookie name返回cookie value
        :param cookie_name: cookie name(key)
        :return:
        '''
        self.driver.delete_cookie(cookie_name)

    def Enca_close_driver(self):
        '''
        关闭浏览器页面,不杀死驱动(程序仍在运行)
        :return:
        '''
        self.driver.close()

    def Enca_quit_driver(self):
        '''
        关闭浏览器页面，同时杀死驱动,程序退出
        :return:
        '''
        self.driver.quit()

    def Enca_uploadWinFile(self, filepath):
        '''
        文件上传
        :param filepath: 文件路径
        :return:
        '''
        pyautogui.write(filepath)
        time.sleep(2)
        pyautogui.press('enter', 2)  # 按2次回车键（按2次是为了防止出错）

    def ele_locator(self, to_element):
        '''
        单元素定位
        :param to_element: xpath定位参数
        :return: 元素对象ele
        '''
        return self.driver.find_element(By.XPATH, to_element)

    # self.ele_locator().is_displayed()  # 判断元素是否展示出来
    # self.ele_locator().is_enabled()  # 判断元素是否可操作
    # self.ele_locator().is_selected()  # 判断元素是否被选中

    # 多元素定位
    def ele_locators(self, to_element):
        return self.driver.find_elements(By.XPATH, *to_element)

    def Enca_click(self, to_element):
        '''
        点击
        :param to_element: 元素对象ele
        :return:
        '''
        return self.ele_locator(to_element).click()

    def Enca_sendkey(self, to_element, sendkey):
        '''
        输入
        :param to_element: 元素对象ele
        :param sendkey: 输入的参数
        :return:
        '''
        return self.ele_locator(to_element).send_keys(sendkey)

    def Enca_clear(self, to_element):
        '''
        清空
        :param to_element: 元素对象ele
        :return:
        '''
        return self.ele_locator(to_element).clear()

    def Enca_select_deselect_all(self, to_element):
        '''
        复选框清空所有
        :param to_element: 元素对象ele
        :return:
        '''
        Select(self.ele_locator(to_element)).deselect_all()

    def Enca_select(self, to_element, type, by):
        '''
        复选框选中
        :param to_element: 元素对象ele
        :param type: 选中方式
        :param by: 根据选中方式输入对应的参数
        :return:
        '''
        if type == 'index':  # 通过索引选中
            Select(self.ele_locator(to_element)).select_by_index(by)
        if type == 'value':  # 通过下拉框value值选中
            Select(self.ele_locator(to_element)).select_by_value(by)
        if type == 'visible_text':  # 通过文本选中
            Select(self.ele_locator(to_element)).select_by_visible_text(by)

    def Enca_scrollintoview(self, to_element):
        '''
        元素聚焦
        :param to_element: 元素对象ele
        :return:
        '''
        target = self.ele_locator(to_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Enca_remove_attribute_readonly(self, byid):
        '''
        去除元素只读
        :param byid:
        :return:
        '''
        js_readonly = f'document.getElementById("{byid}").removeAttribute("readonly");'
        self.driver.execute_script(js_readonly)

    # 页面input框利用send_keys上传图片
    # driver.find_element_by_id("file_select").send_keys("F:\dd.jpg")

    def Enca_get_element_text(self, to_element):
        '''
        获取元素文本
        :param to_element: 元素对象ele
        :return: 文本
        '''
        return self.ele_locator(to_element).text

    # 获取元素属性Value
    def Enca_get_attribute(self, to_element, attr):
        '''
        获取元素属性
        :param to_element: 元素对象ele
        :param attr: 属性key
        :return: 属性value
        '''
        return self.ele_locator(to_element).get_attribute(attr)

    def Enca_tag_name(self, to_element):
        '''
        已知元素定位、获取元素的tagName（元素标签名）
        :param to_element: 元素对象ele
        :return: tagname
        '''
        return self.ele_locator(to_element).tag_name

    def Enca_get_location(self, to_element):
        '''
        获取元素位置
        :param to_element: 元素对象ele
        :return: 位置参数
        '''
        return self.ele_locator(to_element).location

    def Enca_get_elesize(self, to_element):
        '''
        获取元素大小
        :param to_element: 元素对象ele
        :return:
        '''
        return self.ele_locator(to_element).size

    def Enca_submit(self, to_element):
        '''
        <form>表单提交
        :param to_element: 元素对象ele
        :return:
        '''
        self.ele_locator(to_element).submit()

    def execute_script(self, js):
        '''
        执行JS代码
        :param js: 代码块(str)
        :return:
        '''
        self.driver.execute_script(js)

    def Enca_implicitly_wait(self, time=10):
        '''
        隐式等待
        :param time: 等待时间,默认10s
        :return:
        '''
        self.driver.implicitly_wait(time)

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self,locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self,locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def Enca_intelligent_wait(self, on_element, timeout=10):
        '''
        显式等待基本封装,验证元素是否存在于页面DOM树中，存在则返回元素本身，不存在则报错
        # 用法，与WebDriverWait配合使用
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        # 判断当前页面的标题是否符合预期
        title = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道'))
        :param on_element: 元素对象ele
        :param timeout: 等待时间
        :return:
        '''

        WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            EC.presence_of_element_located(self.ele_locator(on_element)))

    # 显式等待常用方式封装
    def Enca_intelligent_wait2(self, on_element, type=0, message="元素未找到", y_or_n=True, is_click=False):
        '''
        :param self: 显示等待
        :param on_element: 定位参数
        :param type: 0为判断元素是否可见，1为判断元素是否加到dom树里
        :param message: 出现错误的提示信息
        :param y_or_n: boolen值，True直到满足条件时退出等待。Flase直到不满足条件时退出等待
        :param is_click: true:点击 false：不点击
        '''
        if y_or_n:
            if type == 0:
                WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(on_element), message)
            elif type == 1:
                WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(on_element), message)
        else:
            if type == 0:
                WebDriverWait(self.driver, 30, 0.5).until_not(EC.visibility_of_element_located(on_element), message)
            elif type == 1:
                WebDriverWait(self.driver, 30, 0.5).until_not(EC.presence_of_element_located(on_element), message)
        if is_click:
            self.ele_locator(on_element).click()

    def get_screen_shot(self, save_path):
        '''
        将当前窗口的屏幕截图保存到PNG图像文件中
        :param save_path: 保存文件路径
        :return:
        '''
        self.driver.get_screenshot_as_file(save_path)

    # 保存截图(截取当前浏览器页面页面)
    def Enca_save_screenshot(self, save_path):
        self.driver.save_screenshot(save_path)

    # 图片流截图(截取当前浏览器页面页面)
    def Enca_get_screenshot_as_png(self, save_path):
        sc_str = self.driver.get_screenshot_as_png()
        with open(save_path, "w") as f:
            f.write(sc_str)

    # BASE64截图
    def Enca_get_screenshot_as_base64(self, save_path):
        sc_str = self.driver.get_screenshot_as_base64()
        html_tmp = """
            <html>
            <body>
    
            <h1>这是一个截图</h1>
            <img src="data:image/png;base64,{}"/>
            </body>
            </html>
            """.format(sc_str)
        with open(save_path, "w") as f:
            f.write(html_tmp)

    def Enca_long_img(self, filepath):
        '''
        截长图/png
        :param filepath: 图片保存你位置
        :return:
        '''
        # 获取浏览器页面的滚动宽度
        width = self.driver.execute_script("return document.documentElement.scrollWidth")
        # 获取浏览器页面的滚动高度
        height = self.driver.execute_script("return document.documentElement.scrollHeight")
        # 修改浏览器窗口大小
        self.driver.set_window_size(width, height)
        # 获取整个网页截图
        self.driver.get_screenshot_as_file(filepath)

    def Enca_scrollTo(self, type, start_num=0, end_number=500):
        '''
        滚动条操作
        :param type: 操作类型:scrollTo(start为起始，end为终点,int类型),scrollHeight(滚动到浏览器底部),scrollTop(滚动到浏览器顶部)
        :param start_num: 自定义设置浏览器滚动位置
        :param end_number:
        :return:
        '''
        if type == 'scrollTo':
            js = f"window.scrollTo({start_num},{end_number});"
            self.driver.execute_script(js)
        if type == 'scrollHeight':
            js = 'window.scrollTo(0,document.body.scrollHeight)'
            self.driver.execute_script(js)
        if type == 'scrollTop':
            js = 'window.scrollTo(0,document.body.scrollTop=0)'
            self.driver.execute_script(js)

    # 键盘操作
    def Enca_keys(self, to_element, keys_type):
        '''
        键盘操作
        :param to_element: 元素对象ele
        :param keys_type: 键位名(小写)
        :return:
        '''
        if keys_type == 'backspace':
            self.ele_locator(to_element).send_keys(Keys.BACK_SPACE)
        elif keys_type == 'tab':
            self.ele_locator(to_element).send_keys(Keys.TAB)
        elif keys_type == 'enter':
            self.ele_locator(to_element).send_keys(Keys.ENTER)
        elif keys_type == 'shift':
            self.ele_locator(to_element).send_keys(Keys.SHIFT)
        elif keys_type == 'ctrl':
            self.ele_locator(to_element).send_keys(Keys.CONTROL)
        elif keys_type == 'alt':
            self.ele_locator(to_element).send_keys(Keys.ALT)
        elif keys_type == 'esc':
            self.ele_locator(to_element).send_keys(Keys.ESCAPE)
        elif keys_type == 'space':
            self.ele_locator(to_element).send_keys(Keys.SPACE)
        elif keys_type == 'page up':
            self.ele_locator(to_element).send_keys(Keys.PAGE_UP)
        elif keys_type == 'page down':
            self.ele_locator(to_element).send_keys(Keys.PAGE_DOWN)
        elif keys_type == 'end':
            self.ele_locator(to_element).send_keys(Keys.END)
        elif keys_type == 'home':
            self.ele_locator(to_element).send_keys(Keys.HOME)
        elif keys_type == 'left':
            self.ele_locator(to_element).send_keys(Keys.LEFT)
        elif keys_type == 'up':
            self.ele_locator(to_element).send_keys(Keys.UP)
        elif keys_type == 'right':
            self.ele_locator(to_element).send_keys(Keys.RIGHT)
        elif keys_type == 'down':
            self.ele_locator(to_element).send_keys(Keys.DOWN)
        elif keys_type == 'insert':
            self.ele_locator(to_element).send_keys(Keys.INSERT)
        elif keys_type == 'delete':
            self.ele_locator(to_element).send_keys(Keys.DELETE)
        elif keys_type == 'ctrla':
            self.ele_locator(to_element).send_keys(Keys.CONTROL, 'a')
        elif keys_type == 'ctrlc':
            self.ele_locator(to_element).send_keys(Keys.CONTROL, 'c')
        elif keys_type == 'ctrlx':
            self.ele_locator(to_element).send_keys(Keys.CONTROL, 'x')
        elif keys_type == 'ctrlv':
            self.ele_locator(to_element).send_keys(Keys.CONTROL, 'v')
        else:
            print('数字及F*未封装')
