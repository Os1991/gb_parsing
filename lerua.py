import scrapy
from ..items import LeruaItem
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse


class LeruaSpider(scrapy.Spider):
    name = 'lerua'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/catalogue/laminat/']

    def parse(self, response: HtmlResponse, **kwargs):
        links = response.xpath('//*[@class="phytpj4_plp largeCard"]/a/@href').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_links)

    def parse_links(self, response: HtmlResponse, **kwargs):
        title = response.xpath('//*[@class="header-2"]/text()').extract_first()
        images = response.xpath('//*[@slot="pictures"]//@src').extract()
        params = response.xpath('//*[@class="def-list"]//text()').extract()
        yield LeruaItem(title=title, images=images, params=params)
