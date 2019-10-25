# -*- coding: utf-8 -*-
import scrapy


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['lovehhy.net']
    start_urls = ['http://lovehhy.net/']

    def parse(self, response):
        pass
