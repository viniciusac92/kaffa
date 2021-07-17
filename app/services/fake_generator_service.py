import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class FoodProvider(BaseProvider):
    def grocery(self):
        groceries = [
            'Café expresso',
            'Capuccino',
            'Irish coffee',
            'Caffè latte',
            'Macchiato',
            'Mocha',
            'Duplo',
            'Coca-cola',
            'Chocolate 50% Cacau',
            'Croissant',
            'Biscoito de nata',
            'Torta Holandesa',
            'Folhado de Frango',
            'Waffle',
            'Pão de Queijo',
            'Bolo de fubá',
        ]

        return random.choice(groceries)


fake.add_provider(FoodProvider)


print(fake.grocery())
