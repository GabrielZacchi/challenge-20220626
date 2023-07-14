from django.urls import path, include
from fitness_foods_lc import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'product', views.ProductsViewSet, r"product")