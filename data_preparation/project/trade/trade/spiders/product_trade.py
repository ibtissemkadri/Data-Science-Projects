# -*- coding: utf-8 -*-
import re
import time
import pandas as pd
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from elasticsearch import Elasticsearch


class ProductTradeSpider(scrapy.Spider):
    name = 'product_trade'
    allowed_domains = ['https://www.trademap.org/']
    start_urls = ['https://www.trademap.org/Product_SelCountry_TS.aspx?nvpm=1|788||||TOTAL|||2|1|1|2|2|1|1|1|1']

    def parse(self, response):
        title=response.xpath("//span[@id='ctl00_Label_Title']/text()").extract()
        reporter=re.findall(r'exported by ([\w\s]+)', title[0])[0]
        outputs=response.xpath("//a[contains(@href,'Sort$output')]//text()").extract()
        year=re.findall(r'\d\d\d\d',' '.join(outputs))
        driver = webdriver.Firefox()
        driver.get(response.url)
        driver.switch_to_active_element
        product_list = driver.find_elements_by_xpath("//table[@id='ctl00_PageContent_MyGridView1']//tr[position() > 2]")
        for co in product_list[:-1]:
            line=' '.join(co.text.split(' ')[1:])
            product=re.findall(r'[\D,\s.\'()_-]*',line)[0].strip()
            vals=line[len(product)+1:].split()
            for i in range(len(vals)):
                driver.switch_to_active_element
                item = {}
                item['partners'] = "All"
                item['reporters'] = reporter
                item['products'] = product
                item['trade_value'] = int((vals[i]+'000').replace(',',''))
                item['years'] = year[i]
                yield item
        links = list(set(response.xpath("//a[contains(@href,'Page$')]//text()").extract()))
        for link in links:
            next_page = driver.find_element_by_link_text(link)
            next_page.click()
            #wait=WebDriverWait(driver, 20)
            #wait.until(elementIdentified(By.id("ctl00_PageContent_MyGridView1")))
            driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS)
            driver.switch_to_active_element
            driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS)
            product_list = driver.find_elements_by_xpath("//table[@id='ctl00_PageContent_MyGridView1']//tr[position() > 2]")
            
            for co in product_list[:-1]:
                driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS)
                time.sleep(20) 
                line=' '.join(co.text.split(' ')[1:])
                product=re.findall(r'[\D,\s.\'()_-]*',line)[0].strip()
                vals=line[len(product)+1:].split()
                for i in range(len(vals)):
                    driver.switch_to_active_element
                    item = {}
                    item['partners'] = "All"
                    item['reporters'] = reporter
                    item['products'] = product
                    item['trade_value'] = int((vals[i]+'000').replace(',',''))
                    item['years'] = year[i]
                    yield item
            time.sleep(2)    
        
        
      
