import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class FoodProvider(BaseProvider):
    def grocery(self):
        groceries = ['Coca-cola', 'Café expresso', 'Chocolata 50% Cacau', 'Croissant', 'Biscoito de nata', 'Torta Holandesa', 'Folhado de Frango', 'Waffle', 'Capuccino', 'Pão de Queijo']
        
        return random.choice(groceries)


fake.add_provider(FoodProvider)


print(fake.grocery())
