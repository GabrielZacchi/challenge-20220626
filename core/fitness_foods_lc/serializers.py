from rest_framework_mongoengine import serializers
from fitness_foods_lc import models

class ProductsSerializers(serializers.DocumentSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'