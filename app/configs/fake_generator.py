import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class FakeProvider(BaseProvider):
    @staticmethod
    def username_kaffa():
        return fake.first_name() + ' ' + str(fake.password(length=9, digits=True))

    @staticmethod
    def product_name():
        return FakeProvider.grocery() + ' ' + str(fake.password(length=9, digits=True))

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
            'Torta holandesa',
            'Folhado de frango',
            'Waffle',
            'Pão de queijo',
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
