# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from quotes_spider.items import QuotesSpiderItem
class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first();
        return FormRequest.from_response(
            response,
            formdata={
                    'csrf_token': token,
                    'password': "Kappa",
                    'username': "123",
            },
            callback = self.scrape_home_page
        )

    def scrape_home_page(self, response):
        open_in_browser(response)
        loader = ItemLoader(item=QuotesSpiderItem(), response=response)
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        loader.add_value('h1_tag', h1_tag )
        loader.add_value('tags', tags)

        return loader.load_item()

        # quotes = response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        #     text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        #     tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
        #
        #
        #     yield {
        #         'Author': author,
        #         'Text': text,
        #         'Tags': tags,
        #     }
        #
        #
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page = response.urljoin(next_page_url)
        # yield scrapy.Request(absolute_next_page)
