# 图片验证码识别
import ddddocr


# 识别图片验证码
def Enca_ddocr(Code_Img_Path):
    ocr = ddddocr.DdddOcr()
    with open(Code_Img_Path, 'rb') as f:
        img_bytes = f.read()
    revfcode = ocr.classification(img_bytes)
    return revfcode

'''
    大致流程
    # 要截图的元素
    element = browser.find_element_by_xpath('//div[@class="a-row a-text-center"]')
    # 坐标
    x, y = element.location.values()
    # 宽高
    h, w = element.size.values()
    # 把截图以二进制形式的数据返回
    image_data = browser.get_screenshot_as_png()
    # 以新图片打开返回的数据
    screenshot = Image.open(BytesIO(image_data))
    # 对截图进行裁剪
    result = screenshot.crop((x, y, x + w, y + h))
    # 显示图片
    # result.show()
    # 保存验证码图片
    result.save('VerifyCode.png')
    # 调用recognize方法识别验证码
    code = recognize('VerifyCode.png')
    print(code)
    # 输入验证码
    browser.find_element_by_name('field-keywords').send_keys(code)
    # 点击确认
    browser.find_element_by_class_name('a-button-text').click()
    time.sleep(1)
'''
