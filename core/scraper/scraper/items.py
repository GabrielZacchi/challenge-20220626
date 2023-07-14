from scrapy_mongoengine_item import MongoEngineItem
from fitness_foods_lc import models
import scrapy

class ProductItem(MongoEngineItem):
    django_model = models.Products
    code = scrapy.Field()
    barcode = scrapy.Field()
    url = scrapy.Field()
    product_name = scrapy.Field()
    quantity = scrapy.Field()
    categories = scrapy.Field()
    packaging = scrapy.Field()
    brands = scrapy.Field()
    image_url = scrapy.Field()