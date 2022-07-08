from frame.log import log

from spiders.SpiderGoldPrice import GoldPrice
from spiders.SpiderManager import SpiderManager

sm = SpiderManager ()
sm.registSpider (GoldPrice())
