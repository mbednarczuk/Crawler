# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item


class ZaraItem(scrapy.Item):
    brand = scrapy.Field()
    category = scrapy.Field()
    colors = scrapy.Field()
    composition = scrapy.Field()
    description = scrapy.Field()
    id = scrapy.Field()
    image = scrapy.Field()
    maintenance = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    url = scrapy.Field()
