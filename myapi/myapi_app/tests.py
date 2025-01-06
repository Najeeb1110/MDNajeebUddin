from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {
            "name": "Test Item",
            "description": "A test item",
            "price": "10.99"
        }
        self.item = Item.objects.create(**self.item_data)

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item(self):
        data = {
            "name": "New Item",
            "description": "A new test item",
            "price": "15.99"
        }
        response = self.client.post('/api/items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
