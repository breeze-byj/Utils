from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 与WebDriverWait配合使用,主要用于断言或浏览器渲染过程中添加等待
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 判断当前页面的标题是否符合预期
title = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道'))

'''判断title是否是一致,返回布尔值'''
WebDriverWait(driver, 10, 0.1).until(EC.title_is("title_text"))

'''判断title是否与包含预期值,返回布尔值'''
WebDriverWait(driver, 10, 0.1).until(EC.title_contains("title_text"))

'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回元素'''
WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((locator)))

'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
WebDriverWait(driver, 10, 0.1).until(EC.visibility_of_element_located((locator)))

'''同上，但是上面的方法时传入locator(定位器)，这个方法是传入element（元素）'''
WebDriverWait(driver, 10, 0.1).until(EC.visibility_of(driver.find_element(locator)))

'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
WebDriverWait(driver, 10, 0.1).until(EC.presence_of_all_elements_located((locator)))

'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''
WebDriverWait(driver, 10, 0.1).until(EC.visibility_of_any_elements_located((locator)))

'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
WebDriverWait(driver, 10, 0.1).until(EC.text_to_be_present_in_element((locator), '预期的text'))

'''判断指定元素的value属性值中是否包含了预期的字符串，返回布尔值(注意：只是value属性)'''
WebDriverWait(driver, 10, 0.1).until(EC.text_to_be_present_in_element_value((locator), '预期的text'))

'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
WebDriverWait(driver, 10, 0.1).until(EC.frame_to_be_available_and_switch_to_it(locator))

'''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
WebDriverWait(driver, 10, 0.1).until(EC.invisibility_of_element_located((locator)))

'''判断某个元素是否可见并且是可点击的，如果是的就返回这个元素，否则返回False'''
WebDriverWait(driver, 10, 0.1).until(EC.element_to_be_clickable((locator)))

'''等待某个元素从dom树中移除'''
WebDriverWait(driver, 10, 0.1).until(EC.staleness_of(driver.find_element(locator)))

'''判断某个元素是否被选中了,一般用在下拉列表'''
WebDriverWait(driver, 10, 0.1).until(EC.element_to_be_selected(driver.find_element(locator)))

'''判断某个元素的选中状态是否符合预期'''
WebDriverWait(driver, 10, 0.1).until(EC.element_selection_state_to_be(driver.find_element(locator), True))

'''判断某个元素的选中状态是否符合预期'''
WebDriverWait(driver, 10, 0.1).until(EC.element_located_selection_state_to_be((locator), True))

'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
accept = WebDriverWait(driver, 10, 0.1).until(EC.alert_is_present())
