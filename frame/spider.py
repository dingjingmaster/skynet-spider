#!/usr/bin/env python
# -*- encoding=utf8 -*-
from frame.get import Get
from frame.log import log
from abc import abstractmethod, ABCMeta


""" 抓取基类 """
class Spider(metaclass=ABCMeta):
    def __init__ (self):
        self._name = 'base spider'
        self._seedURL = ''

    def setUrl (self, url : str):
        if None is not url:
            self._seedURL = url

    def getName (self):
        return self._name

    @abstractmethod
    def run (self): pass

