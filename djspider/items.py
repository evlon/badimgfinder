# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_type = scrapy.Field()
    article_title= scrapy.Field()
    article_url= scrapy.Field()
    img_domain= scrapy.Field()
    img_src= scrapy.Field()
    errors= scrapy.Field()

