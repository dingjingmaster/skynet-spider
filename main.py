#!/usr/bin/env python
# -*- coding=utf-8 -*-
from frame.log import log
from spiders.SpiderManager import SpiderManager
from frame.thread import ThreadPool


if __name__ == '__main__':
    log.info('抓取任务开始执行 ...')

    sm = SpiderManager()

    tpool = ThreadPool()
    spiders = sm.getRegistedSpider()
    log.info ("已注册爬虫共 %d 个" % len(spiders))
    for spider in spiders:
        tpool.setSpider (spider)
    tpool.run()

    log.info('抓取任务执行完毕 !!!')

    exit(0)
