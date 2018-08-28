# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BadimgSpider(CrawlSpider):
    name = 'badimg'

    allowed_domains = ['your.site.domain.com.com']
    start_urls = ['your.site.domain.com.com']

    rules = [
        #导航条CSS选择器
        Rule(LinkExtractor(allow=r'',restrict_css='div.sitemap > ul > li > a',), callback='parse_site', follow=True), 
        #子栏目新闻列表选择器
        Rule(LinkExtractor(allow=r'',restrict_css='div.menu.container > div.nav.fl > ul > li > a',), callback='parse_item', follow=True),
        #下一页 选择器
        Rule(LinkExtractor(allow=r'',restrict_xpaths='//div[@class="page"]/a[text()="下一页"]',), callback='parse_item', follow=True),

        #文章内图片选择器
        Rule(LinkExtractor(allow=r'',restrict_css='div.m2newList > ul > li > a',), callback='parse_article', follow=True),        
        ]
    def parse_site(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def parse_article(self, response):
        title = response.xpath('//*[@id="title"]/text()').extract()
        article = response.url
        htmluri = urllib.parse.urlparse(response.url)
        #bad_img = []
        for imgsrc in response.xpath('//img/@src').extract():
            if(imgsrc.startswith("//")):
                imgsrc = htmluri.scheme + ":" + imgsrc
            elif(imgsrc.startswith("/")):
                imgsrc = htmluri.scheme + "://" + htmluri.netloc + imgsrc;          
            imguri = urllib.parse.urlparse(imgsrc)
            item  = {"item_type":"imgurl","article_title":title, "article_url":article, "img_domain": imguri.netloc.lower(), "img_src": imgsrc, "errors":[]}
            yield  item
     

