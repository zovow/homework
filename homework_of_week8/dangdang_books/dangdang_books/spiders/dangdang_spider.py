import scrapy

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    start_urls = ['https://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%CA%E9%BC%AE&act=input']

    def parse(self, response):
        books = response.css('.bigimg li')

        for book in books:
            title = book.css('.name a::text').get()
            price = book.css('.price span::text').get()

            yield {
                'title': title,
                'price': price,
            }

        # 获取下一页的链接并继续爬取
        next_page = response.css('.paging .num:last-child + a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
