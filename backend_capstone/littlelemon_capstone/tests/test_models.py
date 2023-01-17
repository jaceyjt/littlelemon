from django.test import TestCase
from Restaurant.models import Menu
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Chocolate", price="2.33", inventory=16)
        self.assertEqual(str(item), "Chocolate : 2.33")