from django.test import TestCase
from django.urls import reverse
from .models import Item

class ItemViewTest(TestCase):
    # Set up data for tests
    def setUp(self):
        # Create a test item in the database
        self.item = Item.objects.create(name="Test Item", description="Test Description", price=9.99)

    # Test item list view
    def test_item_list_view(self):
        # Use Django's test client to simulate an HTTP request to the item list view
        response = self.client.get(reverse('item_list'))
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Ensure that the list view contains the name of the item we created
        self.assertContains(response, "Test Item")

    # Test item detail view
    def test_item_detail_view(self):
        # Use Django's test client to request the detail page for the item we created
        response = self.client.get(reverse('item_detail', args=[self.item.id]))
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Ensure the detail view contains the name of the item
        self.assertContains(response, self.item.name)
        self.assertContains(response, self.item.description)
