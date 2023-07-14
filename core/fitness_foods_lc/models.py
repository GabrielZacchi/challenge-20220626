from mongoengine import Document, fields
from enum import Enum
import datetime
class Status(str, Enum):
    DRAFT = 'draft'
    IMPORTED = 'imported'
class Products(Document):
    code = fields.IntField(min_value=0, unique=True)
    barcode = fields.StringField()
    status = fields.EnumField(Status, default='draft')
    imported_t = fields.DateTimeField()
    url = fields.URLField()
    product_name = fields.StringField()
    quantity = fields.StringField()
    categories = fields.StringField()
    packaging = fields.StringField()
    brands = fields.StringField()
    image_url = fields.URLField()

    def save(self, *args, **kwargs):
        if not self.imported_t:
            self.imported_t = datetime.datetime.now()
        
        if self.status == 'draft':
            self.status = 'imported'
        
        # Check if the document already exists in the database
        if self.code:
            existing_product = Products.objects(code=self.code).first()
            if existing_product:
                return existing_product.update(**self.to_mongo())
        
        return super(Products, self).save(*args, **kwargs)