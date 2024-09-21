from django.test import TestCase
from restaurant.models import MenuItem
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(item, "Ice Cream : 80")