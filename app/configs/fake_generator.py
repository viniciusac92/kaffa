import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class FakeProvider(BaseProvider):
    @staticmethod
    def grocery():
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

    @staticmethod
    def payment_method():
        payment_methods = [
            'Cartão crédito',
            'Cartão débito',
            'Dinheiro',
        ]

        return random.choice(payment_methods)


fake.add_provider(FakeProvider)
