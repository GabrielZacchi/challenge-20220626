from fitness_foods_lc import models
import re 

class ScraperPipeline(object):
    def process_item(self, item, spider):
        product = models.Products(**item)
        product.save()
        return item


