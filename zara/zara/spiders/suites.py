from ..items import ZaraItem
import scrapy



class SuitesSpider(scrapy.Spider):
    name = 'suites'
    allowed_domains = ['www.zara.com']
    start_urls = ['https://www.zara.com/pl/pl/kobieta-garnitury-l1437.html?v1=781046']

    def parse(self, response):
        res = response.xpath("//div/ul/li/a[class='item _item']/@href").extract()
        print("-------------123--------------------")
        for sel in res:
            yield scrapy.Request(sel, self.parse_product_detail)
            print(res)
            print(sel)

    def parse_product_detail(self, response):
        brand = "ZARA"
        category = ''
        colors = response.xpath("//p[@class='color']/span[@class='_colorName']/text()").extract_first()
        composition = response.xpath("//p[@class='list-composition']/text()").extract()
        description = response.xpath("//p[@class='description']/text()").extract_first()
        id = response.xpath("//p[@class='reference']/text()").extract_first()
        image = "https:" + response.xpath(
            "//div[@class='media-wrap image-wrap']/a/img[@class='image-big _img-zoom']/@src").extract_first()
        maintenance = response.xpath("//p[@class='list-cares']/text()").extract()
        name = response.xpath("//h1[@class='product-name']/text()").extract_first().strip()
        price = response.xpath("//div[@class='price _product-price']/span/text()").extract_first()
        size = response.xpath("//div[@class='g-radio-btn']/label/text()").extract_first()
        url = response.url

        item = ZaraItem(
            brand=brand,
            category = category,
            colors=colors,
            composition=composition,
            description=description,
            id=id,
            image=image,
            maintenance=maintenance,
            name=name,
            price=price,
            size=size,
            url=url,
        )
        yield item
