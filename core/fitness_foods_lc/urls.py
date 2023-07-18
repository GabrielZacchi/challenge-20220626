from fitness_foods_lc import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'products', views.ProductsViewSet, r"products")