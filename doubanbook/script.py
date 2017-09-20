# coding:utf-8
import threading

from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings
from twisted.internet import reactor


def run_douban():
    settings = Settings({
        'BOT_NAME': 'book9',

        'SPIDER_MODULES': ['doubanbook.book9.spiders'],
        'NEWSPIDER_MODULE': 'doubanbook.book9.spiders',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'FEED_URI': u'.//douban.csv',
        'FEED_FORMAT': 'CSV'

    })
    runner = CrawlerRunner(settings)

    d = runner.crawl('dbbook')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return 0


# 下面的代码仅共参考，实际上直接run_csbk() 也可以
def thread_douban():
    print("--------------")
    threading.Thread(target=run_douban())


if __name__ == '__main__':
    thread_douban()
