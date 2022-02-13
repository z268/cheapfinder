import scrapy


class DnsSpider(scrapy.Spider):
    name = 'dns'
    allowed_domains = ['www.dns-shop.ru']
    start_urls = ['https://www.dns-shop.ru/']

    def parse(self, response):
        pass
