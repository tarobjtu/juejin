# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from juejin import settings
from juejin.items.likes import LikesItem
from juejin.items.article import ArticleItem


# 保存数据到MySQL数据库
class MySQLPipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()


    def close_spider(self, spider):
        self.connect.close()


    def process_item(self, item, spider):

        if item.__class__ == LikesItem:
            sql = 'insert into juejin.Likes(user_id, user_name, followers, likes, pv, updated_at) \
                   values (%s, %s, %s, %s, %s, %s)'

            try:
                self.cursor.execute(sql, (
                        item['user_id'],
                        item['user_name'],
                        item['followers'],
                        item['likes'],
                        item['pv'],
                        item['updated_at']
                    )
                )
                self.connect.commit()

            except Exception,e:
                print '插入数据库表出错：%s' %(e)
                self.connect.rollback()

        return item
