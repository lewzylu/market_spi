# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BuffItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    market_hash_name = scrapy.Field()
    sell_num = scrapy.Field()
    id = scrapy.Field()
    sell_min_price = scrapy.Field()
    steam_price = scrapy.Field()
    game = scrapy.Field()
    pass
