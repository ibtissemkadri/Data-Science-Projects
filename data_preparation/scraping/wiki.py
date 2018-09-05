# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['www.wiki.tn']
    start_urls = ['https://www.wiki.tn/pc-portable-120.html']

    def parse(self, response):
        products=response.xpath("//div[contains(@class,'ajax_bloc')]")
        #links =response.xpath("//div[contains(@class,'ajax_bloc')]//a[@class='product-name']/@href").extract()
            #price =
        for product in products:
        #for link in links:
            link=product.xpath(".//a[@class='product-name']/@href").extract()[0]
            yield scrapy.Request(link, self.parse_item)#, meta=['price':price])
        
        next_page = response.xpath("//li[@class='pagination_next']/a/@href").extract()
        if next_page:
            yield scrapy.Request('https://www.wiki.tn'+next_page[0], self.parse)

    def parse_item(self,response):
        #price = response.meta['price']
        #name=response.xpath('//h1[@itemprop="name"]/text()').extract()
        #ref=response.xpath('//p[@id="product_reference"]/label/span/text()').extract()
        #brand=response.xpath('//span[@class="marque"]/img/@title').extract()
        #price=response.xpath('//span[@id="our_price_display"]/@data-price').extract()
        #pc_dict={'name':name[0], 'ref':ref, 'brand':brand[0], 'price':float(price[0])}
        #print(pc_dict.items())
        print('Processing..' + response.url)
