from selenium.webdriver import ActionChains
from Driver_Funcation import DriverFuncation


# 对 ActionChains 类进行封装，调用操作（元素）方法，再执行 perform() 方法
# 作用: 模拟鼠标点击事件
class ActionChainsFuncation(DriverFuncation):
    def __init__(self):
        '''
        继承于 DriverFuncation obj
        '''
        super().__init__()
        self.action = ActionChains(self.driver)

    def Enca_click(self, on_element):
        '''
        点击鼠标左键
        :param on_element: 元素对象ele
        :return:
        '''
        self.action.click(on_element).perform()

    def Enca_double_click(self, on_element):
        '''
        双击鼠标左键
        :param on_element:元素对象ele
        :return:
        '''
        self.action.double_click(on_element).perform()

    def Enca_click_and_hold(self, on_element):
        '''
        点击鼠标左键，不松开
        :param on_element:元素对象ele
        :return:
        '''
        self.action.click_and_hold(on_element).perform()

    def Enca_context_click(self, on_element):
        '''
        点击鼠标右键
        :param on_element:元素对象ele
        :return:
        '''
        self.action.context_click(on_element).perform()

    def Enca_drag_and_drop(self, source_element, target_elemrnt):
        '''
        拖拽到某个元素然后松开
        :param source_element: 被拖拽元素
        :param target_elemrnt: 目标元素
        :return:
        '''
        self.action.drag_and_drop(source_element, target_elemrnt).perform()

    # 拖拽到某个坐标然后松开
    def Enca_drag_and_drop_by_offset(self, source_element, xoffset, yoffset):
        '''

        :param source_element: 被拖拽元素
        :param xoffset: 目标坐标 x
        :param yoffset: 目标坐标 y
        :return:
        '''
        self.action.drag_and_drop_by_offset(source_element, xoffset, yoffset).perform()

    def Enca_move_by_offset(self, xoffset, yoffset):
        '''
        鼠标从当前位置移动到某个坐标
        :param xoffset: 目标坐标 x
        :param yoffset: 目标坐标 y
        :return:
        '''
        self.action.move_by_offset(xoffset, yoffset).perform()

    def Enca_move_to_element_with_offset(self, to_element, xoffset, yoffset):
        '''
        移动到距某个元素（左上角坐标）多少距离的位置
        :param to_element:元素对象ele
        :param xoffset:
        :param yoffset:
        :return:
        '''
        self.action.move_to_element_with_offset(to_element, xoffset, yoffset).perform()

    def Enca_release(self, on_element):
        '''
        在某个元素位置松开鼠标左键
        :param on_element:元素对象ele
        :return:
        '''
        self.action.release(on_element).perform()

    def Enca_pause(self, seconds):
        '''
        暂停操作（s）
        :param seconds: time
        :return:
        '''
        self.action.pause(seconds).perform()

    def Enca_perform(self):
        '''
        执行鼠标操作方法
        :return:
        '''
        self.action.perform().perform()

    def Enca_reset_actions(self):
        '''
        清除已在队列中的鼠标操作命令
        :return:
        '''
        self.action.reset_actions().perform()

    def Enca_key_down(self, key, element):
        '''
        在元素位置按下键盘按钮
        :param key: 键位
        :param element: 目标元素
        :return:
        '''
        self.action.key_down(key, element).perform()

    def Enca_key_up(self, key, element):
        '''
        在元素位置松开键盘按钮
        :param key:键位
        :param element: 目标元素
        :return:
        '''
        self.action.key_up(key, element).perform()

    # 发送某个键到当前焦点的元素
    def Enca_send_keys(self, *keys_to_send):
        '''

        :param keys_to_send:
        :return:
        '''
        self.action.send_keys(*keys_to_send).perform()

    # 发送某个键到指定元素
    def Enca_send_keys_to_element(self, element, *keys_to_send):
        '''

        :param element:元素对象ele
        :param keys_to_send:
        :return:
        '''
        self.action.send_keys_to_element(element, *keys_to_send).perform()


if __name__ == '__main__':
    ac = ActionChainsFuncation()
    ac.driver.get("https://cloud.lixiaotech.com/trialviz")
