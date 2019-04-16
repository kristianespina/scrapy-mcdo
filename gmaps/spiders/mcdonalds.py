# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider

class McdonaldsSpider(CrawlSpider):
    name = 'mcdonalds'
    allowed_domains = ['google.com', 'mcdonalds.de']
    start_urls = ['mcdonalds.de']

    '''
    rules = (
        Rule(LinkExtractor(allow=(),
        restrict_xpaths=('//*[@id="pnnext"]')), callback='parse_item', follow=True),
    )
    '''
    def parse_item(self, response):
        dformat = 'street h#, postalcode city'
        item = {}
        #print(response)
        links = response.xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div/div/div/div/a/@href')
        for link in links:
            url = link.get()
            if test_link(url):
                item['link'] = url
                yield item
            #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
            #item['name'] = response.xpath('//div[@id="name"]').get()
            #item['description'] = response.xpath('//div[@id="description"]').get()
            #yield item
