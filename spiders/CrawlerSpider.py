from typing import Any
import scrapy
from scrapy.http import Response

class CrawlerSpider(scrapy.Spider):
    name = "metaCrawler"
    start_urls = [
        'https://www.metacritic.com/game/'
    ]
    def parse(self, response) :
        title = response.css('title::text').extract()
        title1 = response.xpath("//title::text").extract()
        yield{'TitleText ' : title}
    