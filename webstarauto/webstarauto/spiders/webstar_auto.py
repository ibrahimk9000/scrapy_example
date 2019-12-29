# -*- coding: utf-8 -*-
import scrapy


class WebstarAutoSpider(scrapy.Spider):
    name = 'webstar-auto'
    allowed_domains = ['webstar-auto.com']
    start_urls = ['http://webstar-auto.com/']
    
    def parse(self, response):
         for href in response.css('.item1.produit_titre a'):
            l=href.css('a::attr(href)').get()
            h=href.css('h3::text').get()
            yield response.follow(l, self.parse_car,cb_kwargs=dict(h3=h))
            

    def parse_car(self, response,h3):
         li=[]

         for ca in response.css('.item_okaz_block'):

          li.append({
            'model': ca.css('h3::text').get(),
              'price': ca.css('span.prix + span::text').get(),
         })
         return {h3:li}