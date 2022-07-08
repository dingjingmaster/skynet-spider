#!/usr/bin/env python
# -*- coding=utf-8 -*-
import threading
from frame.log import log
from frame.spider import Spider

"""
SpiderManager 主要用来做爬虫管理，所有爬虫都会注册到其中
"""
class SpiderManager(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass 

    def __new__(cls, *args, **kwargs):
        if not hasattr(SpiderManager, "_instance"):
            with SpiderManager._instance_lock:
                if not hasattr(SpiderManager, "_instance"):
                    SpiderManager._instance = object.__new__(cls)
                    SpiderManager._spiders = {}
        return SpiderManager._instance

    def registSpider(self, spider : Spider):
        if None is spider: return
        name = spider.getName()
        if name not in self._spiders:
            self._spiders[name] = spider
            log.info("regist spider '%s' successed!", name)

    def getRegistedSpider(self):
        return self._spiders.values()
