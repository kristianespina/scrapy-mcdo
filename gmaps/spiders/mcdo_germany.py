# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re

class McdoGermanySpider(scrapy.Spider):
    name = 'mcdo-germany'
    allowed_domains = ['mcdonalds.de']
    start_urls = ['http://mcdonalds.de/']

    def parse(self, response):
        links = list(range(1,2000))
        for _id in links:
            url = 'https://www.mcdonalds.de/restaurant?id={}'.format(_id)
            yield Request(url, callback=self.parse_direct)

    def parse_direct(self, response):
        item = {}
        pattern = r'([^0-9]+)([^\d]+(\d?(-)?\d.*)), (\d+) (.*)'
        telephone_pattern = r'Tel.: (\+(.*))'
            # 1 = street
            # 3 = house number
            # 5 = zip code
            # 6 = city 
        elem = response.xpath('//div[@class="headline"]/h3/text()').extract()
        try:
            address = re.match(pattern, elem[0])

            item['id_source'] = 'https://mcdelivery.de/'
            item['url'] = response.request.url
            item['name'] = 'McDonald\'s'
            item['address'] = elem[0].strip()
            item['street'] = address[1].strip()
            item['house_number'] = address[3].strip()
            item['postal_code'] = address[5].strip()
            item['city'] = address[6].strip()
            item['country'] = 'DE'
            item['phone_number'] = re.match(telephone_pattern, elem[2].strip())[1]
            item['flag_match'] = None
            item['flag_menu'] = None
            item['flag_coca_opp'] = None
            item['flag_meal'] = None
            item['flag_drink'] = None
            item['source'] = None
            item['website'] = None
            item['kitchen'] = None
            item['category'] = None
            item['rating'] = None
            item['reviews_nr'] = None
            item['latitude'] = None
            item['longitude'] = None
            #item['name'] = elem[1].strip()
            
            yield item
        except:
            pass