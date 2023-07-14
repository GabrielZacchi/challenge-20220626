from rest_framework_mongoengine import viewsets
from fitness_foods_lc import models, serializers
class ProductsViewSet(viewsets.ModelViewSet):
    lookup_field = 'code'
    serializer_class = serializers.ProductsSerializers

    def get_queryset(self):
        return models.Products.objects.all()