# -*- coding: utf-8 -*-
import scrapy


class JumiaSpider(scrapy.Spider):
    name = 'jumia'
    #allowed_domains = ['https://www.jumia.dz/']
    #start_urls = ['https://www.jumia.dz/']
    pg=0
    def start_requests(self):
        
        url = 'https://www.jumia.dz/'
        attr = getattr(self, 'catg', 'smartphones/')
        pgn = getattr(self, 'pg', 5)
        self.pg=int(pgn)
        url = url  + attr
        yield scrapy.Request(url=url, callback=self.parse)
        
    
    def parse(self, response):
        for hl in response.css('.sku.-gallery  a.link::attr(href)').getall():
            yield response.follow(hl, self.parsei)
        next=response.css('a[title=Suivant]::attr(href)').get()
        if self.pg>0:
         self.pg=self.pg-1
         yield response.follow(next, self.parse)
         

    def parsei(self, response):
            
         yield {'spec':response.css('h1.-fs20.-pts.-pbxs::text').get(),
                'price':response.css('span.-b.-ltr.-tal.-fs24::text').get(),
               }


            
