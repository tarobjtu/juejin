# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    title = scrapy.Field()
    likes = scrapy.Field()
    comments = scrapy.Field()
    updated_at = scrapy.Field()
