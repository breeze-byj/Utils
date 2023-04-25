from urllib import request, parse
# 导入urllib.error包中 HTTPError,URLError 模块   异常捕获
from urllib.error import HTTPError, URLError
# 导入 cookiejar 保存cookie
from http import cookiejar


class session(object):
    def __init__(self):
        # 通过对象保存cookie
        cookie_object = cookiejar.CookieJar()
        # handler 对应着一个操作
        handler = request.HTTPCookieProcessor(cookie_object)
        # opener 遇到有cookie的response的时候
        # 调用handler内部的一个函数，存储到cookie object
        self.opener = request.build_opener(handler)

    # 重新构建get请求调用下面def get的函数
    def get(self, url, headers=None):
        return get(url, headers, self.opener)

    # 重新构建post请求调用下面def post的函数
    def post(self, url, form, headers=None, ):
        return post(url, form, headers, self.opener)


# 再次封装 如果是get请求直接调用 get(url,headers=None) ###headers可不写
# a.get(url,headers=None)
def get(url, headers=None, opener=None):
    return urlrequests(url, headers=headers, opener=opener)


# 再次封装 如果是post请求直接调用 post(url,form,headers=None) ### headers可不写
def post(url, form, headers=None, opener=None):
    return urlrequests(url, form, headers=headers, opener=opener)


# 1. 传入url
# 2. user_agent
# 3. headers
# 4. 定义Request
# 5. urlopen
# 6. 返回byte数组
def urlrequests(url, form=None, headers=None, opener=None):
    # 判断headers是否存在，如果不存在使用自定义headers
    if headers == None:
        headers = {
            'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    html_bytes = b''  # 倒成二进制bytes格式
    try:
        # 如果form存在，为post请求执行if内程序
        if form:
            # POST
            # 2.1转换成str
            form_str = parse.urlencode(form)
            # 2.2转换成bytes
            from_bytes = form_str.encode('utf-8')
            req = request.Request(url, data=from_bytes, headers=headers)
        # 如果form不存在，为get请求执行else内程序
        else:
            # get
            req = request.Request(url, headers=headers)
        # 判断是否所有opener（cookie)
        # 如果有将直接执行opener.open()
        if opener:
            response = opener.open(req)  # 第二个参数设置为timeout 如果请求超时会报出except URLError错误
        # 如果没有opener（cookie)
        # 将按正常请求执行
        else:
            response = request.urlopen(req)
        html_bytes = response.read()
    except HTTPError as a:
        print(a)
    except URLError as e:
        print(e)
    except Exception as s:
        print(s)
    return html_bytes


if __name__ == '__main__':
    # url = 'http://fanyi.baidu.com/sug'
    # form = {
    #     'kw': '呵呵'
    # }
    # html_bytes = post(url, form=form)
    # print(html_bytes)

    url = 'http://www.baidu.com'  # 写入想要爬取的网站地址
    html_bytes = get(url)
    print(html_bytes.decode('utf-8'))
