import csv
from datetime import datetime

from app.configs.database import db
from app.configs.fake_generator import FakeProvider
from app.reports import DATABASE_PATH_SALES
from faker import Faker
from flask_sqlalchemy.model import Model
from ipdb import set_trace

fake = Faker()


def verify_missing_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]


def verify_recieved_keys(data: dict, key_list: list) -> list:
    data_keys = data.keys()

    return [key for key in data_keys if key not in key_list]


def add_all_commit(list_model: list[Model]) -> None:
    db.session.add_all(list_model)
    db.session.commit()


def add_commit(model: Model) -> None:
    db.session.add(model)
    db.session.commit()


def delete_commit(model: Model) -> None:
    db.session.delete(model)
    db.session.commit()


def get_all(model: Model):
    return db.session.query(model).all()


def get_one(model: Model, id: int):
    return model.query.get(id)


def update_model(model: Model, data: dict) -> None:
    for key, value in data.items():
        setattr(model, key, value)
    add_commit(model)


def create_fake_user(amount: int):
    return {
        "username": FakeProvider.username_kaffa(),
        "type": fake.random_int(min=1, max=3),
        "password": "1234",
        "name": fake.name(),
        "cpf": str(fake.random_number(digits=9, fix_len=True)),
    }


def create_fake_product(amount: int):
    return {
        "name": FakeProvider.product_name(),
        "description": fake.sentence(nb_words=10, variable_nb_words=False),
        "price": fake.pyfloat(
            left_digits=2, right_digits=2, positive=True, max_value=100
        ),
        "stock": fake.random_int(min=1, max=40),
    }


def create_fake_provider(amount: int):
    return {
        "trading_name": fake.company(),
        "cnpj": str(fake.random_number(digits=14, fix_len=True)),
        "phone": str(fake.random_number(digits=9, fix_len=True)),
    }


def create_fake_purchase_order(amount: int):
    from app.services import ManagerServices, ProviderServices

    providers = ProviderServices.get_all_providers()
    managers = ManagerServices.get_all_managers()

    return {
        "id_manager": fake.random_int(min=1, max=len(managers)),
        "id_provider": fake.random_int(min=1, max=len(providers)),
        "date": fake.past_date(start_date='-30d', tzinfo=None),
    }


def create_fake_tables():
    from app.services import TableServices

    tables = TableServices.get_all_tables()

    while len(tables) < 5:
        return {"number": fake.random_int(min=1, max=100)}

    return None


def create_fake_cashier():
    from app.services import CashierServices

    cashiers = CashierServices.get_all_cashiers()

    if len(cashiers) != 0:
        return None

    return {"initial_value": fake.random_int(min=50, max=250), "balance": 0}


def create_fake_payment_methods():
    from app.services import PaymentMethodServices

    payment_method = PaymentMethodServices.get_all_payment_method()

    if len(payment_method) != 0:
        return None

    return {
        "name": FakeProvider.payment_method(),
        "description": fake.sentence(nb_words=10, variable_nb_words=False),
    }


def create_fake_account(amount: int):
    from app.services import (
        CashierServices,
        PaymentMethodServices,
        TableServices,
        WaiterServices,
    )

    cashiers = CashierServices.get_all_cashiers()
    waiters = WaiterServices.get_all_waiters()
    tables = TableServices.get_all_tables()
    payment_methods = PaymentMethodServices.get_all_payment_method()

    return {
        "date": str(datetime.now().strftime('%d/%m/%Y')),
        "id_cashier": fake.random_int(min=1, max=len(cashiers)),
        "id_waiter": fake.random_int(min=1, max=len(waiters)),
        "id_table": fake.random_int(min=1, max=len(tables)),
        "id_payment_method": fake.random_int(min=1, max=len(payment_methods)),
    }


def create_fake_account_product(account_data: dict):
    from app.services import ProductServices

    products = ProductServices.get_all_products()

    return {
        'id_account': str(account_data['id']),
        'id_product': fake.random_int(min=1, max=len(products)),
        'quantity': fake.random_int(min=1, max=3),
    }


def create_sales_report(account_list: list):
    fieldnames = [
        'waiter_id',
        'waiter_name',
        'account_number',
        'account_status',
        'product',
        'product_price',
        'quantity_ordered',
        'product_sales_income',
    ]

    report_data_list = [
        {fieldnames: data for fieldnames, data in zip(fieldnames, data)}
        for data in account_list
    ]

    with open(DATABASE_PATH_SALES, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_data_list)
