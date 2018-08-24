# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/Users/samiperalahti/withinsights/chrome-extension/node_modules/chromedriver/lib/chromedriver/chromedriver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()

        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)

    def parse_book(self, response):
        pass




# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
#
#
# class BooksSpider(CrawlSpider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/']
#
#     # lin extactor arguments:
#     #  deny_domains=('google.com') does not scrape these pages
#     #  allow=('music') only scrapes these pages
#     rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=False),)
#
#     def parse_page(self, response):
#         yield { 'URL': response.url }
