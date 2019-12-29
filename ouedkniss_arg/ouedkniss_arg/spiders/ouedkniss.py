# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ouedkniss_arg.items import ouedkniss_argItem

class OuedknissSpider(scrapy.Spider):
    name = 'ouedkniss'
    allowed_domains = ['www.ouedkniss.com']
     
    def start_requests(self):
        urls=[]
        url = 'http://www.ouedkniss.com/'
        attr = getattr(self, 'catg', 'informatique/ordinateur-portable/')
        url = url  + attr
           
        attr = getattr(self, 'pg', 5)
        for i in range(1,int(attr)):
            urls.append(url+str(i))
            
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for hl in response.css('li.annonce_titre  a::attr(href)').getall():
            yield response.follow(hl, self.parsei)
            
    

    def parsei(self, response):
            itm = ouedkniss_argItem()
           
            itm['title']=response.css('#Title::text').get()
            itm['disc']=response.css('#GetDescription::text').get()
            itm['price']=response.css('span[itemprop="price"]::text').get()
            yield itm

            
