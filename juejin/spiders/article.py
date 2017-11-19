# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from juejin.items.article import ArticleItem
from juejin.utils.common import now, extract_number

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['juejin.im']
    start_urls = ['https://juejin.im/user/59659aff5188250cf956e6dd']

    def parse(self, response):
        sel = Selector(response)
        item = ArticleItem()

        user_name = sel.xpath('//div[@class="username"]/text()').extract_first()
        titles = sel.xpath('//div[@class="row abstract-row"]/a[@class="title"]').extract()
        likes = sel.xpath('//ul[@class="action-list"]/li/span[@class="count"]').extract()
        comments = sel.xpath('//li[@class="action comment clickable"]/span[@class="count"]').extract()

        item['user_id'] = '59659aff5188250cf956e6dd'
        item['user_name'] = user_name

        item['updated_at'] = now()
        return item
