from django.test import TestCase
from .models import Product
class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Apple")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Apple")

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Apple")
