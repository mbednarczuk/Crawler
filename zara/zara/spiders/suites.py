# -*- coding: utf-8 -*-
import scrapy



class SuitesSpider(scrapy.Spider):
    name = 'suites'
    # allowed_domains = ['www.zara.com/pl/']
    start_urls = ['https://www.zara.com/pl/pl/kobieta-garnitury-l1437.html?v1=781046']


