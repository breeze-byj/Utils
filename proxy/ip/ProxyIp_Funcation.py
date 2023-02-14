# 网络资源
import queue
import requests
from lxml import etree
from fake_useragent import UserAgent
import threading

# 从网上copy的代码,后续有需要可以作为参考


url_list = [f'https://www.89ip.cn/index_{page}.html' for page in range(1, 150)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0/Firefox 54.0/Windows/Computer/Common'}


def crawl(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    return html


def parse(html):  ##解析并测试IP是否可用
    ips_list = html.xpath('//table/tbody/tr/td[1]/text()')
    ports_list = html.xpath('//table/tbody/tr/td[2]/text()')
    for ip_, port in zip(ips_list, ports_list):
        proxy = ip_.strip() + ":" + port.strip()
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy)
        }
        try:

            resp = requests.get(url='http://httpbin.org/get', proxies=proxies, headers=headers, timeout=3)
            # 状态码为200 的就写入文件并输出到控制台
            if resp.status_code == 200:
                print(proxy, '\033[31m可用\033[0m')
                with open('代理IP.txt', 'a') as f:
                    f.write(proxy)
                    f.write('\r\n')
            else:
                print(proxy, '不可用')
        except:
            print(proxy, '不可用')


def do_crawl(url_queue: queue.Queue, html_queue: queue.Queue):
    url = url_queue.get()
    html = crawl(url)
    html_queue.put(html)


def do_pares(html_queue: queue.Queue):
    html = html_queue.get()
    parse(html)


if __name__ == "__main__":

    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in url_list:
        url_queue.put(url)
    for i in range(100):
        t = threading.Thread(target=do_crawl, args=(url_queue, html_queue))
        t.start()
    for i in range(100):
        t = threading.Thread(target=do_pares, args=(html_queue,))
        t.start()
