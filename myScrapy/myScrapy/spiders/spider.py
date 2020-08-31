"""
@Copyright: Copyright (c) 2020 苇名一心 All Rights Reserved.
@Project: xuetangzaixian
@Description: 
@Version: 
@Author: 苇名一心
@Date: 2020-04-08 20:31
@LastEditors: 苇名一心
@LastEditTime: 2020-04-08 20:31
"""
import scrapy
import re
from myScrapy.myScrapy.items import MyscrapyItem


class mySpider(scrapy.spiders.Spider):
    name = "xuetang"
    allowed_domains = ["www.xuetangx.com/"]

    start_urls = ["http://www.xuetangx.com/partners"]

    # def parse(self, response):
    #     item = MyscrapyItem()
    #     for each in response.xpath("/html/body/article[1]/section/ul/*"):
    #         item['school'] = each.xpath("a/div[2]/h3/text()").extract()
    #         item['num'] = each.xpath("a/div[2]/p[1]/text()").extract()
    #         if item['num']:
    #             item['num'] = re.findall(r'\d+', item['num'][0])
    #         if item['school'] and item['num']:
    #             yield (item)
    def parse(self, response):
        item = MyscrapyItem()
        for i in range(1, 144):
            item['school'] = response.xpath \
                ("/html/body/article[1]/section/ul/li[{}]/a/div[2]/h3/text()".format(i)).extract()
            item['num'] = response.xpath \
                ("/html/body/article[1]/section/ul/li[{}]/a/div[2]/p[1]/text()".format(i)).extract()
            if item['school'] and item['num']:
                yield (item)
