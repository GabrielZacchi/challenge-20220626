from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fitness_foods_lc.models import Products
import mongoengine

class ProductsViewSetTests(APITestCase):
    
    @classmethod
    def setUpClass(cls):
        return
    
    @classmethod
    def tearDownClass(cls):
        mongoengine.disconnect()

    def _fixture_setup(self):
        # Create test data
        self.product1 = Products(
            code=1,
            barcode="123456789",
            url="http://example.com/products/1",
            product_name="Product 1",
            quantity="1 kg",
            categories="food",
            packaging="box",
            brands="Brand 1",
            image_url="http://example.com/images/product1.jpg"
        )
        self.product1.save()

        self.product2 = Products(
            code=2,
            barcode="987654321",
            url="http://example.com/products/2",
            product_name="Product 2",
            quantity="500 g",
            categories="food",
            packaging="bag",
            brands="Brand 2",
            image_url="http://example.com/images/product2.jpg"
        )
        self.product2.save()

    def test_get_all_products(self):
        # Test retrieving all products
        url = reverse('products-list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product(self):
        # Test retrieving specific product information
        url = reverse('products-detail', args=[self.product1.code])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.product1.code)
        self.assertEqual(response.data['product_name'], self.product1.product_name)

    def test_get_non_existent_product(self):
        # Test retrieving information for a non-existent product
        url = reverse('products-detail', args=[1000])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def _post_teardown(self):
        return
