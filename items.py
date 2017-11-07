# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixiapiderItem(scrapy.Item):

    job_name = scrapy.Field()
    update_time = scrapy.Field()
    day_money = scrapy.Field()
    city = scrapy.Field()
    education = scrapy.Field()
    days = scrapy.Field()
    months = scrapy.Field()
    attraction = scrapy.Field()
    content = scrapy.Field()
    close_date = scrapy.Field()
    company = scrapy.Field()
    company_addr = scrapy.Field()
    company_url = scrapy.Field()
