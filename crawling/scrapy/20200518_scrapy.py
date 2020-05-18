
# Introduction  scrapy

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
            'http://quotes.toscrape.com/tag/humor/'
            ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                    'author': quote.xpath('span/small/text()').get(),
                    'text': quote.css('span.text::text').get()
                    }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

            
'''
오늘은 scrapy의 공식 문서에 있는 기본 중의 기본 코드를 다루었다. scrapy에서 제공하는 기본 class를 상속받아 사용한다는 개념을 알게 되었다.
그런데 내가 그동안 기존에 사용하던 selenium 방식과는 다르게 어떤식으로 debugging하는지 궁금하다. 다음은 기본 tutorial을 거치면서 기본 class
들에 대해서 배워봐야겠다.
'''
