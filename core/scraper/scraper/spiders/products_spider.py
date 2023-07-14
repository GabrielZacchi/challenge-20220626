from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst

from scraper.scraper.items import ProductItem

class ProductsSpider(CrawlSpider):
    name = "products"
    #allowed_domains = ["openfoodfacts.org"]
    start_urls = [
        "https://world.openfoodfacts.org/"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=("product")),
            callback="parse_product",
            follow=True,
        ),
    )

    def parse_product(self, response):
        product_loader = ItemLoader(item=ProductItem(), response=response)
        product_loader.default_output_processor = TakeFirst()

        url = response.request.url

        product_code = url.split('/')[-2]

        product_barcode = str(product_loader.get_css('#barcode::text')[0]) + str(product_loader.get_xpath('//*[@id="barcode_paragraph"]/text()[2]')[0]).strip()

        product_loader.add_value(
            "code", product_code
        )

        product_loader.add_value(
            "barcode", product_barcode
        )

        product_loader.add_value(
            "url", url
        )

        product_loader.add_css(
            "product_name", "#product > div > div > div.card-section > div > div.medium-8.small-12.columns > h2::text"
        )

        yield product_loader.load_item()