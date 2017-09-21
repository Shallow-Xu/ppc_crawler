# coding:utf-8
import threading

from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings
from twisted.internet import reactor


def run_csbk():
    settings = Settings({
        'BOT_NAME': 'qiubai',
        'SPIDER_MODULES': ['qiubai.hot_text.spiders'],
        'NEWSPIDER_MODULE': 'qiubai.hot_text.spiders',
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36",

        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 3,
        'ITEM_PIPELINES': {
            'qiubai.hot_text.pipelines.WebcrawlerScrapyPipeline': 300,  # 保存到mysql数据库
            'qiubai.hot_text.pipelines.JsonWithEncodingPipeline': 300,  # 保存到文件中
        },
        'AUTOTHROTTLE_START_DELAY': 5,
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_DBNAME': 'ppc',  # 数据库名字，请修改
        'MYSQL_USER': 'root',  # 数据库账号，请修改
        'MYSQL_PASSWD': '12345678',  # 数据库密码，请修改
        'MYSQL_PORT': 3306,  # 数据库端口，在dbhelper中使用

    })
    runner = CrawlerRunner(settings)

    d = runner.crawl('qiubai')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return 0


# 下面的代码仅共参考，实际上直接run_csbk() 也可以
def thread_qiubai():
    print("--------------")
    threading.Thread(target=run_csbk())


if __name__ == '__main__':
    thread_qiubai()
