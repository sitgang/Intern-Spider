# -*- coding: utf-8 -*-
import scrapy
from shixiapider.items import ShixiapiderItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ShixiSpider(CrawlSpider):
    name = "shixi"
    allowed_domains = ["shixiseng.com"]
    start_urls = [
        "http://www.shixiseng.com/interns?p=%d"%i for i in range(1,501)
    ]
    
    rules = (
        Rule(LinkExtractor(allow=(".*/intern/.*", )), callback='parse_item'),
    )
    
    def parse_item(self, response):
        item = ShixiapiderItem()
        job_name = response.xpath('//span[@class="job_name"]/text()').extract()[0]
        update_time = response.xpath('///span[@class="update_time"]/text()').extract()[0]
        day_money = response.xpath('//span[@class="daymoney"]/text()').extract()[0]
        city = response.xpath('//span[@class="city"]/text()').extract()[0]
        education = response.xpath('//span[@class="education"]/text()').extract()[0]
        days = response.xpath('//span[@class="days"]/text()').extract()[0]
        months = response.xpath('//span[@class="month"]/text()').extract()[0]
        attraction = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/p/text()').extract()[0]
        content = ' '.join(response.xpath('//div[@class="dec_content"]/text()').extract())
        content += ' '.join(response.xpath('//div[@class="dec_content"]//p/span/text()').extract())
        close_date = response.xpath('//p[@class="date"]/text()').extract()[0]
        company = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/p[1]/a/text()').extract()[0]
        company_addr = response.xpath('//*[@id="container"]/div[1]/div[2]/div[3]/p/span/text()').extract()[0]
        company_url = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/p[4]/a/@href').extract()[0]
        print job_name,update_time,day_money,city ,education,days,months ,attraction
        print content, close_date,company
        print company_addr,company_url
        item['job_name'] =job_name
        item['update_time'] =update_time
        item['day_money'] =day_money
        item['city'] =city
        item['education'] =education
        item['days'] =days
        item['months'] =months
        item['attraction'] =attraction
        item['content'] =content
        item['close_date'] =close_date
        item['company'] =company
        item['company_addr'] =company_addr
        item['company_url'] =company_url
        return item
#命令行命令 
#cd shixiapider
#scrapy crawl shixi -o items.json
#处理爬取到的数据
#import json 
#with open('/Users/xuegeng/shixiapider/items.json') as f:
#    a = json.load(f)
#import pandas
#pandas.options.display.max_rows = 10
#df = pandas.read_json('/Users/xuegeng/shixiapider/items.json')
#df = df.applymap(lambda x:x.replace('\n','').replace(u'\u4e28',u'').strip())