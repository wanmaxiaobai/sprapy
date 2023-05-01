from pathlib import Path

import scrapy
from tutorial.items import TutorialItem
from tutorial.items import TutorialLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     Path(filename).write_bytes(response.body)
    #     self.log(f'Saved file {filename}')



    def parse(self, response):

        for quote in response.css('div.quote'):
        #     item = TutorialItem
        #     text = quote.css('span.text::text').get(),
        #     author = quote.css('small.author::text').get(),
        #     tags = quote.css('div.tags a.tag::text').getall(),
        #     item['text'] = text
        #     item['author'] = author
        #     item['tags'] = tags
        #     yield item
            itemloader = TutorialLoader(response=response)
            itemloader.add_css('text', 'span.text::text')
            itemloader.add_css('author', 'small.author::text')
            itemloader.add_css('tags', 'div.tags a.tag::text')
        yield itemloader.load_item()