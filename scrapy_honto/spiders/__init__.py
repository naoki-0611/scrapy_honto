# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from datetime import datetime
from pprint import pprint
import scrapy
from scrapy_honto.items import ScrapyHontoItem

class ScrapyTestSpider(scrapy.Spider):
    name = 'scrapy_test_spider'
    allowed_domains = ['honto.jp']
    start_urls = ['https://honto.jp/ranking/gr/bestseller_1101_1201_011_029004000000.html', 'https://honto.jp/ranking/gr/bestseller_1101_1201_011_029004000000.html?tpcl=3']
    # start_urls = ['https://honto.jp/ranking/gr/bestseller_1101_1201_011_029004000000.html']
    # dt = datetime.datetime.now()

    def parse(self, response):
        # return ScrapyHontoItem(
        #     title = response.css('title').extract_first().strip(),
        # )

        # book_titles = response.css('h2.stHeading').extract()
        # pprint(book_titles) 

        # for title in response.css('div.stBoxLine01').extract():
        # # items に定義した ScrapyHontoItem のオブジェクトを生成して次の処理へ渡す
        #     yield ScrapyHontoItem(
        #         url = ??,
        #         book_title = response.css('h2.stHeading a::text').extract():
        #         rank_num = response.css('p.stNum a::text').extract():
        #         date_time = dt
        #     )

        for title in response.css('h2.stHeading a::text').extract():
        # items に定義した ScrapyHontoItem のオブジェクトを生成して次の処理へ渡す
            yield ScrapyHontoItem(
                book_title =title
            )
            
        pass