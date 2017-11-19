# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from juejin.items.likes import LikesItem
from juejin.utils.common import now, extract_number


class LikesSpider(scrapy.Spider):
    name = 'likes'
    allowed_domains = ['juejin.im']
    start_urls = ['https://juejin.im/user/59659aff5188250cf956e6dd']

    def parse(self, response):
        sel = Selector(response)
        user = sel.xpath('//div[@class="username"]/text()').extract_first()
        followers = sel.xpath('//div[@class="user-meta followed-state"]/text()').extract_first()
        likes = sel.xpath('//div[@class="share-state-detail"]/span[1]/text()').extract_first()
        pv = sel.xpath('//div[@class="share-state-detail"]/span[2]/text()').extract_first()
        item = LikesItem()
        item['followers'] = extract_number(followers)
        item['likes'] = extract_number(likes)
        item['pv'] = extract_number(pv)
        item['user_id'] = '59659aff5188250cf956e6dd'
        item['user_name'] = user
        item['updated_at'] = now()
        return item
