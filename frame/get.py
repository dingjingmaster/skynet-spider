#!/usr/bin/env python
# -*-encoding=utf8-*-
import os
import time
import random
import pyquery
import requests

from frame.log import log


class Get:
    def __init__ (self, url: str, try_time=9, try_sec=2):
        self._url = url
        self._try_time = try_time
        self._try_sec = try_sec
        self._proxy = ''
        self._header = {
            'User-Agent':      random.choice(self.__ua),
            'Accept'            : 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control'     : 'no-cache', 
            'Connection'        : 'close',
        }
        self._delProxy()

    def setProxy (self, proxy=''):
        if None is not proxy and '' != proxy:
            os.environ['ALL_PROXY'] = proxy
            os.environ['all_proxy'] = proxy
        elif '' != self._proxy:
            os.environ['ALL_PROXY'] = self._proxy
            os.environ['all_proxy'] = self._proxy

    def hasProxy (self) -> bool:
        if 'ALL_PROXY' in os.environ or 'all_proxy' in os.environ:
            return True
        return False

    def _delProxy (self):
        if not self.hasProxy():
            return
        del os.environ['ALL_PROXY']
        del os.environ['all_proxy']

    def setHeader (self, key : str, value : str):
        if None is not key and None is not value:
            self._header[key] = value

    def html (self) -> str:
        tm = 0
        text = ''
        retry = 1
        while tm <= self._try_time:
            try:
                s = requests.Session()
                s.headers = self._header
                r = s.get(self._url, timeout=10, allow_redirects=True)
                if r.status_code == requests.codes.ok:
                    doc = pyquery.PyQuery(r.text.encode(r.encoding))
                    text = doc.html()
                    break
                s.close()
            except Exception as e:
                log.warning("尝试第 %d 次 获取uri '%s' 失败, 错误信息: %s . 请求头:\n%s\n"
                        % (retry, self._url, str(e), (s.headers)))
                retry += 1
                time.sleep(self._try_sec)
            tm += 1
        return text

    def binary (self):
        tm = 0
        binary = None
        retry = 1
        while tm <= self._try_time:
            try:
                s = requests.Session()
                s.headers = self._header
                r = s.get(self._url, timeout=10, allow_redirects=True)
                if r.status_code == requests.codes.ok:
                    binary = r.content
                    if None is not binary:
                        break
                    break
                s.close()
            except Exception as e:
                log.warning("尝试第 %d 次 获取uri '%s' 失败, 错误信息: %s . 请求头:\n%s\n"
                        % (retry, self._url, str(e), (s.headers)))
                retry += 1
                time.sleep(self._try_sec)
            tm += 1
        return binary

    __ua = [
        'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
    ]


if __name__ == '__main__':
    pass
