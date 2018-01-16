# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from lxml import etree
from urllib import request
#
import time

import requests


class HzfcdataSpider(Spider):
    name = 'hzfcdata'
    allowed_domains = ['www.hzfc.gov.cn/scxx/']
    start_urls = ['http://www.hzfc.gov.cn/scxx/']

    def start_requests(self):
        yield Request(url='http://www.hzfc.gov.cn/scxx/',callback=self.parse,dont_filter=True)
    
    def saveImg(self,imageUrl,fileName):
        #self.browser.get(imageUrl)
        #data = self.browser.page_source
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        r = requests.get(imageUrl,headers=headers)
        data = r.content
        dir = './images/'
        with open(dir + fileName,'wb') as file:
            file.write(data)
        
    def parse(self, response):
        body = response.body.decode('utf-8')
        print('------------------------------')
        selector = etree.HTML(body) #/html/body/div[5]/div[1]/dl/dd/marquee/img
        totalImageurls = selector.xpath('//div[@class="scxx_01_left"]/dl/dd/marquee/img/@src')
        imageurls = selector.xpath('//div[@class="scxx_03"]/dl/dd/img/@src') 
        totalImageurls.extend(imageurls)
        baseurl = 'http://www.hzfc.gov.cn/scxx/'
        fileNames = ['total.png','new.png','old.png']
        datetime = time.strftime('%Y%m%d',time.localtime(time.time()))
        for (url,filename) in zip (totalImageurls,fileNames):
            imageurl = baseurl + url
            print(imageurl)
            self.saveImg(imageurl,datetime + '_' + filename)
        print('after resopnse------------------------------')
    
