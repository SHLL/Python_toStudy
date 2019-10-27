# -*- coding: utf-8 -*-

# 记录学习至  https://www.bilibili.com/video/av57909837/?p=3  该看p4 p3之后  RZT：191027
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['lovehhy.net']
    start_urls = ['http://www.lovehhy.net/Yulu/Detail/ALL/1']
 
    def parse(self, response):
        # selectorList
        duanzidivs = response.xpath("//div[@class='cat_llb']")
        for duanzidiv in duanzidivs:
            # Selector
            bt = duanzidiv.xpath("//*[@id='footzoon']/a/text()").getall()
            context = duanzidiv.xpath("//*[@id='endtext']/text()").getall()
            bt = "".join(bt).strip() + "\n"
            context = "".join(context).strip() + "\n"
            print(bt)
            print(context)
        # print("="*40)
        # print(type(cat_llb))
        # print("="*40)