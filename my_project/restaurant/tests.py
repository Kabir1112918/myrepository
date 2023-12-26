from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description="wow very delicious")
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
