# -*- coding: utf-8 -*-
import scrapy


class VirtuemartSpider(scrapy.Spider):
    name = 'virtuemart'
    allowed_domains = []
    def start_requests(self):
        url='http://demo.virtuemart.net/administrator/index.php'
        
        yield scrapy.Request(url=url,cookies={'58181e506087049198f4a988632c4b3a': 'a7i69sfnuic2el4s8e2n2mm5r0'}, callback=self.parse)

    def parse(self, response):
        with open('body.htm', 'wb') as f:
            f.write(response.body)
