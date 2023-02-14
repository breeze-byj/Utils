from http.cookiejar import MozillaCookieJar
from urllib import request
from urllib.request import HTTPCookieProcessor

# 保存cookie到本地文件或是发送请求时使用已保存的cookie
def Enca_cookies(type, url, cookie_path='./cookies.txt', ):
    '''
    cookie处理
    :param type: 处理类型: get(获取)/use(使用)
    :param url: 目标url
    :param cookie_path: cookie文件路径
    :return: 相应 html
    '''
    cookie = MozillaCookieJar(cookie_path)
    hander = HTTPCookieProcessor(cookie)
    opener = request.build_opener(hander)
    if type == 'get_cookies':
        opener.open(url)
        cookie.save(ignore_discard=True, ignore_expires=True)
    elif type == 'use_cookies':
        cookie.load(filename=cookie_path)
        return opener.open(url).read().decode('utf-8')
