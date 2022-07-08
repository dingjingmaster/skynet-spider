#!/usr/bin/env python
# -*- encoding=utf8 -*-
import threading

from frame.spider import Spider
from frame.log import log


class ThreadPool:
    _stop = False
    _thread = []
    _spider = []
    _thread_count = 10
    _mutex = threading.Lock()

    def setPoolNum (self, num: int):
        if num > self._thread_count:
            self._thread_count = num
        if self._thread_count > 100:
            self._thread_count = 100
        return self

    def setSpider (self, sp: Spider):
        self._mutex.acquire()
        self._spider.append(sp)
        self._mutex.release()

    def working (self, thread_id: int):
        while True:
            if self._mutex.acquire():
                spider: Spider = None
                spiderName = ''
                if len(self._spider) > 0:
                    spider = self._spider.pop()
                    spiderName = spider.getName()
                    log.info('成功获取spider: %s' % spiderName)
                self._mutex.release()
                if spider is not None:
                    log.info('spider: %s 开始执行 !!!' % spiderName)
                    spider.run()
                    log.info('spider: %s 执行完成 !!!' % spiderName)
                else:
                    break

    def run (self):
        """ 先添加，也可不添加 """
        for i in range(0, self._thread_count):
            t = ThreadPool.Thread(self.working, i + 1)
            self._thread.append(t)
        for i in self._thread:
            i.start()
        for i in self._thread:
            i.join()

    class Thread(threading.Thread):
        def __init__ (self, route, tid: int):
            threading.Thread.__init__(self)
            self._tid = tid
            self._route = route

        def run (self):
            self._route(self._tid)
