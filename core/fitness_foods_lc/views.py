from rest_framework_mongoengine import viewsets
from fitness_foods_lc import models, serializers
class ProductsViewSet(viewsets.ModelViewSet):
    lookup_field = 'code'
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializers