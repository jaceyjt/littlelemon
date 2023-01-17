from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Sundae", price=3.33, inventory=12)
        Menu.objects.create(title="Suya", price=1.20, inventory=100)
        Menu.objects.create(title="Pizza", price=20, inventory=11)
    
    def test_getall(self):
        sundae = Menu.objects.get(title="Sundae")
        sundae = MenuSerializer(sundae)

        suya = Menu.objects.get(title="Suya")
        suya = MenuSerializer(suya)


        pizza = Menu.objects.get(title="Pizza")
        pizza = MenuSerializer(pizza)

        sundae = sundae.data
        del sundae["id"]
        self.assertEqual(sundae, {"title": "Sundae", "price": "3.33", "inventory": 12})

        suya = suya.data
        del suya["id"]
        self.assertEqual(suya, {"title": "Suya", "price": "1.20", "inventory": 100})

        pizza = pizza.data
        del pizza["id"]
        self.assertEqual(pizza, {"title": "Pizza", "price": "20.00", "inventory": 11})