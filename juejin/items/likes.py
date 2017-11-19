# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LikesItem(scrapy.Item):
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    followers = scrapy.Field()
    likes = scrapy.Field()
    pv = scrapy.Field()
    updated_at = scrapy.Field()
