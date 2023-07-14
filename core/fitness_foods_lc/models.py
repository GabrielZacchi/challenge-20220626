from mongoengine import Document, fields
from enum import Enum
import datetime
class Status(str, Enum):
    DRAFT = 'draft'
    IMPORTED = 'imported'
class Products(Document):
    code = fields.IntField(min_value=0)
    barcode = fields.StringField()
    status = fields.EnumField(Status, default='draft')
    imported_t = fields.DateTimeField()
    url = fields.URLField(null=True)
    product_name = fields.StringField(null=True)
    quantity = fields.StringField(null=True)
    categories = fields.StringField(null=True)
    packaging = fields.StringField(null=True)
    brands = fields.StringField(null=True)
    image_url = fields.URLField(null=True)

    def save(self, *args, **kwargs):
        if not self.imported_t:
            self.imported_t = datetime.datetime.now()
        return super(Products, self).save(*args, **kwargs)