# -*- coding: utf-8 -*-
import re
import scrapy
import time
from scrapy.http import FormRequest
from selenium import webdriver
from trade.items import TradeItem
from elasticsearch import Elasticsearch
from datetime import datetime


elastic_connection = Elasticsearch('localhost:9200', timeout=3000.0)
counter=0

class TrademapSpider(scrapy.Spider):
    name = 'trademap'
    allowed_domains = ['www.trademap.org/']
    #start_urls = ['https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|788||||85|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|504||||85|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|620||||85|||2|1|1|2|2|1|2|1|1','https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|788||||62|||2|1|1|2|2|1|2|1|1']
    #start_urls=['https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|504||||62|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|792||||62|||2|1|1|2|2|1|2|1|1','https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|818||||62|||2|1|1|2|2|1|2|1|1']
    start_urls = ['https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|788||||080410|||6|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|682||||080410|||6|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|818||||080410|||6|1|1|2|2|1|2|1|1']
    #start_urls=['https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|012||||27|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|818||||27|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|788||||TOTAL|||2|1|1|2|2|1|2|1|1', 'https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1|788||||27|||2|1|1|2|2|1|2|1|1']
    counter=0
    retailers="trademap"
    
    def parse(self, response):
            title=response.xpath("//span[@id='ctl00_Label_Title']/text()").extract()
            reporter=re.findall(r'exported by ([\w\s]+)', title[0])[0]
            sub_title = response.xpath("//span[@id='ctl00_Label_SubTitle']/text()").extract()
            product = re.findall(r'\d\s([\D\s]+),', sub_title[0])
            if product:
                product=product[0]
            else:
                product=sub_title[0].split(':')[1].strip()
            outputs=response.xpath("//a[contains(@href,'Sort$output')]//text()").extract()
            year=re.findall(r'\d\d\d\d',' '.join(outputs))
            table=response.xpath("//table[@id='ctl00_PageContent_MyGridView1']//tr[position() > 2]")
            for ta in table:
                co=ta.xpath(".//a/text()").extract()
                if co:
                    vals=ta.xpath(".//td[position() > 2]//text()").extract()
                    for i in range(len(vals)):
                        item = {}
                        item['partners'] = co[0]
                        item['reporters'] = reporter
                        item['years'] = year[i]
                        item['trade_values'] = int((vals[i]+'000').replace(',',''))
                        item['product']=product
                        item['retailers']=self.retailers
                        yield item
               
                        doc_id = "%s-%s-%s"%('trademap.org',time.time(),self.counter)
                        self.counter+=1
                        elastic_connection.index(index='trademap',doc_type='export',id= doc_id, body=item)
            urls=list(set(response.xpath("//a[contains(@href,'Page$')]//text()").extract()))
            driver = webdriver.Firefox()
            driver.get(response.url)
            
            for url in urls:
                link=driver.find_element_by_link_text(url)
                link.click()
                driver.switch_to.active_element
                da=driver.find_elements_by_xpath("//table[@id='ctl00_PageContent_MyGridView1']\
                                                   //tr[position() > 2]")
                for co in da[:-1]:
                    country=re.findall(r'[\D,\s.\'()_-]*',co.text)[0].strip()
                    vals=co.text[len(country)+1:].split()
                    for i in range(len(vals)):
                        item = {}
                        item['partners'] = country
                        item['reporters'] = reporter
                        item['years'] = int(year[i])
                        item['trade_values'] = int((vals[i]+'000').replace(',',''))
                        item['product']=product
                        item['retailers']=self.retailers
                        yield item
                        doc_id = "%s-%s-%s"%('trademap.org',time.time(),self.counter)
                        self.counter+=1
                        elastic_connection.index(index='trademap',doc_type='export',id= doc_id, body=item)

