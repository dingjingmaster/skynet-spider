#!/usr/bin/env python
# -*- coding=utf-8 -*-
from frame.get import Get
from frame.log import log
from frame.spider import Spider

import json

""" 抓取国际金价 """
class GoldPrice(Spider):
    def __init__ (self):
        self._name = 'international gold price'
        self._seedURL = 'https://data-asg.goldprice.org/dbXRates/USD,CNY'

    def run (self):
        js = Get(self._seedURL)
        js.setHeader('Content-Type', 'application/x-www-form-urlencoded')
        if None is not js:
            jsStr = js.binary()
            if None is jsStr : return

            js1 = json.loads (jsStr)
            if None is js1 : return

            timeStamp = ''
            auCNY = ''
            auUSD = ''
            agCNY = ''
            agUSD = ''

            def getAu0Ag (json1) -> (str, str):
                au, ag = '', ''
                if 'xauPrice' in json1:
                    au = json1['xauPrice']
                if 'xagPrice' in json1:
                    ag = json1['xagPrice']
                return (au, ag)

            if 'ts' in js1:
                timeStamp = str(js1['ts'])[:10]

            items = []
            if 'items' in js1:
                items = js1['items']

            for item in items:
                if 'curr' not in item:
                    continue
                if 'CNY' == item['curr']:
                    auCNY, agCNY = getAu0Ag (item)
                elif 'USD' == item['curr']:
                    auUSD, agUSD = getAu0Ag (item)
            # 输出金价
            log.info ("\n金价、银价抓取结果:\n"
                    "中国金价/盎司: %s\n"
                    "美国金价/盎司: %s\n"
                    "中国银价/盎司: %s\n"
                    "美国银价/盎司: %s\n"
                    "时间: %s\n" % (auCNY, auUSD, agCNY, agUSD, timeStamp))
        return
