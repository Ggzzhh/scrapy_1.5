# -*- coding: utf-8 -*-
import requests
import time
import threading
import queue
import redis
from bs4 import BeautifulSoup


class Proxies:
    """
    获取 西刺免费代理IP， 快代理， 无忧代理， 云代理 的可用代理
    响应时间在2秒内
    存储到txt中
    """
    def __init__(self):
        self.redis = redis.StrictRedis(decode_responses=True)
        self.http = []
        self.https = []
        self.max_threads = 20
        self.queue = queue.Queue()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

    def run(self):
        """
        进行验证并且存储到给定的文件中去
        """
        start_ips = time.time()
        print('------开始获取所有免费代理地址-------')
        self.get_ips()
        end_ips = time.time()
        print('------获取结束, 总耗时：{:.2f}s-------'.format(end_ips - start_ips))

        print('------开始验证可用代理-------')
        start_verf = time.time()
        threads = []
        while not self.queue.empty():
            for thread in threads:
                if not thread.is_alive():
                    # 移除停止活动的线程
                    threads.remove(thread)
            while len(threads) < self.max_threads:
                porxy = self.queue.get()
                thread = threading.Thread(target=self.go_verify, args=(porxy,))
                thread.setDaemon(True)
                thread.start()
                threads.append(thread)
        end_verf = time.time()
        print('------验证结束，总耗时：{:.2f}s-------'.format(end_verf - start_verf))

        # with open('http.txt', 'w') as f:
        #     for proxy in self.http:
        #         f.write(proxy['http'] + '\n')
        #
        # with open('https.txt', 'w') as f:
        #     for proxy in self.https:
        #         f.write(proxy['https'] + '\n')
        # 清除两个键
        self.redis.delete('http', 'https')
        for i in self.http:
            self.redis.lpush('http', i['http'])

        for i in self.https:
            self.redis.lpush('https', i['https'])

        print('------存储完毕，存储地址为：{} 以及 {}------'
              .format('redis:http', 'redis:https'))

    def get_ips(self):
        """运行所有获取免费ip的函数"""
        xici = threading.Thread(self.proxy_xici())
        xici.start()

        wuyou = threading.Thread(self.proxy_wuyou())
        wuyou.start()

        kuai = threading.Thread(self.proxy_kuai())
        kuai.start()

        yun = threading.Thread(self.proxy_yun())
        yun.start()

    def go_verify(self, proxies):
        """验证代理是否可用"""
        if proxies.get('http'):
            url = 'http://dl.3dmgame.com/pc/cn'
        else:
            url = 'https://dl.3dmgame.com/pc/cn'
        try:
            requests.get(url, proxies=proxies, timeout=2.01)
        except:
            # print('代理: {} 请求超时'.format(proxies))
            return False
        else:
            if proxies.get('http'):
                self.http.append(proxies)
            else:
                self.https.append(proxies)

    def proxy_xici(self):
        """抓取xici代理中的高匿代理"""
        base_url = 'http://www.xicidaili.com/nn/{}'
        for i in range(1, 4):
            time.sleep(0.5)
            res = requests.get(base_url.format(i), headers=self.headers)
            soup = BeautifulSoup(res.text, 'lxml')
            trs = soup.find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                proxy = {str(tds[5].text).lower(): str(tds[1].text) + ':' + str(
                    tds[2].text)}
                self.queue.put(proxy)

    def proxy_kuai(self):
        """抓取快代理中的免费代理"""
        base_url = 'https://www.kuaidaili.com/free/inha/{}/'
        for i in range(1, 5):
            time.sleep(1)
            res = requests.get(base_url.format(i), headers=self.headers)
            soup = BeautifulSoup(res.text, 'lxml')
            trs = soup.find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                self.queue.put({str(tds[3].text).lower(): str(tds[0].text) +
                                ':' + str(tds[1].text)})

    def proxy_wuyou(self):
        """抓取无忧代理中的免费代理"""
        urls = [
            'http://www.data5u.com/free/gngn/index.shtml',
            'http://www.data5u.com/free/gnpt/index.shtml',
            'http://www.data5u.com/free/gwgn/index.shtml',
            'http://www.data5u.com/free/gwpt/index.shtml'
        ]
        for url in urls:
            time.sleep(1)
            res = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(res.text, 'lxml')
            trs = soup.find_all('ul', attrs={'class': 'l2'})
            for tr in trs:
                tds = tr.find_all('span')
                self.queue.put({str(tds[3].text).lower(): str(tds[0].text) +
                                ':' + str(tds[1].text)})

    def proxy_yun(self):
        """抓取云代理中的免费代理"""
        base_url = 'http://www.ip3366.net/?stype={}&page={}'
        for i in range(1, 5):
            for x in range(1, 5):
                time.sleep(0.5)
                res = requests.get(base_url.format(i, x), headers=self.headers)
                soup = BeautifulSoup(res.text, 'lxml')
                trs = soup.find_all('tr')
                for tr in trs[1:]:
                    tds = tr.find_all('td')
                    self.queue.put({str(tds[3].text).lower(): str(tds[0].text) +
                                    ':' + str(tds[1].text)})

if __name__ == '__main__':
    t = Proxies()
    t.run()
