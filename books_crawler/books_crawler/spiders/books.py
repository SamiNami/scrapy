# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.http import Request



class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']


    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url =response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        pass
#
# class BooksSpider(Spider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#
#     def start_requests(self):
#         self.driver = webdriver.Chrome('/Users/samiperalahti/withinsights/chrome-extension/node_modules/chromedriver/lib/chromedriver/chromedriver')
#         self.driver.get('http://books.toscrape.com')
#
#         sel = Selector(text=self.driver.page_source)
#         books = sel.xpath('//h3/a/@href').extract()
#
#         for book in books:
#             url = 'http://books.toscrape.com/' + book
#             yield Request(url, callback=self.parse_book)
#
#         while True:
#             try:
#                 next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
#                 sleep(3)
#                 self.logger.info("Sleeping for 3 seconds")
#                 next_page.click()
#
#                 sel = Selector(text=self.driver.page_source)
#                 books = sel.xpath('//h3/a/@href').extract()
#
#                 for book in books:
#                     url = 'http://books.toscrape.com/catalogue/' + book
#                     yield Request(url, callback=self.parse_book)
#
#             except NoSuchElementException:
#                 self.logger.info("No more pages to load.")
#                 self.driver.quit()
#                 break
#
#
#     def parse_book(self, response):
#         pass


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
