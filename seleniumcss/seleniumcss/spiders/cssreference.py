# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector

from selenium.webdriver.common.keys import Keys

class CssreferenceSpider(scrapy.Spider):
    name = 'cssreference'
  #  allowed_domains = ['https://cssreference.io']
    start_urls = ['https://cssreference.io/']

    def __init__(self):
        self.chrome = webdriver.Chrome("/home/ibrahim/Downloads/chromedriver")
    
    
       
    def closed(self):
         self.chrome.close()

        

    def parse(self, response):
        self.chrome.get(response.url)
        elem = self.chrome.find_element_by_id("finder-input")
        elem.clear()
        elem.send_keys("flex")
        time.sleep(1)
        source = self.chrome.page_source # get source of the loaded page
        sel = Selector(text=source)
        
        for hl in sel.css('.finder-item.is-highlighted a.finder-item-link::attr(href)').getall():
            
            yield scrapy.Request(url=hl, callback=self.parsei)
        


    def parsei(self, response):
        #join <p>text<code>text</code>text</p>
        yield {'title':''.join(response.css('.property-name a::text').getall()).strip(),      
        'desc':''.join(response.css('.property-description *::text').getall()).strip(),
        }
