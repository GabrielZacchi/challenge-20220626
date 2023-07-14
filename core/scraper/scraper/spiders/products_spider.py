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

        product_barcode = str(response.xpath('//*[@id="barcode_paragraph"]/text()[1]').get()).strip()

        type_product_barcode = str(response.xpath('//*[@id="barcode_paragraph"]/text()[2]').get()).strip()

        product_name = str(response.css('#product > div > div > div.card-section > div > div.medium-8.small-12.columns > h2::text').get()).strip()

        categories = str(response.xpath('string(//*[@id="field_categories_value"])').get()).strip()

        packaging = str(response.xpath('string(//*[@id="field_packaging_value"])').get()).strip()

        brands = str(response.xpath('string(//*[@id="field_brands_value"])').get()).strip()

        product_loader.add_value(
            "code", product_code
        )

        product_loader.add_value(
            "barcode", str(product_barcode + type_product_barcode)
        )

        product_loader.add_value(
            "url", url
        )

        product_loader.add_value(
            "product_name", product_name
        )

        product_loader.add_css(
            "quantity", "#field_quantity_value::text"
        )

        product_loader.add_value(
            "categories", categories
        )

        product_loader.add_value(
            "packaging", packaging
        )

        product_loader.add_value(
            "brands", brands
        )

        yield product_loader.load_item()