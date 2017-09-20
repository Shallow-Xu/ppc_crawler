# -*- coding: utf-8 -*-
import scrapy
from qiubai.hot_text.items import WebcrawlerScrapyItem


class SpiderTxt(scrapy.Spider):
    name = "qiubai"  # 定义爬虫名，要和settings中的BOT_NAME属性对应的值一致
    allowed_domains = ["qiushibaike.com"]
    start_urls = ["https://www.qiushibaike.com/text/",
                  "https://www.qiushibaike.com/text/page/2/",
                  "https://www.qiushibaike.com/text/page/3/",
                  "https://www.qiushibaike.com/text/page/4/",
                  "https://www.qiushibaike.com/text/page/5/"]

    def parse(self, response):
        for item in response.xpath(
                '//div[@id="content-left"]/div[starts-with(@class,"article block untagged mb15") and @id]'):
            qiubai = WebcrawlerScrapyItem()

            url = item.xpath('@id').extract()
            if url:
                url = url[0].split('_')[2]
                qiubai['url'] = url

            content = item.xpath('./a[1]/div[@class="content"]/descendant::text()').extract()
            if content:
                con = ''
                for str in content:
                    con += str
                qiubai['content'] = con

            yield qiubai
