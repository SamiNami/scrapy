# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # lin extactor arguments:
    #  deny_domains=('google.com') does not scrape these pages
    #  allow=('music') only scrapes these pages
    rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=False),)

    def parse_page(self, response):
        yield { 'URL': response.url }
