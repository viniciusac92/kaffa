import click
from app.services import (
    AccountProductServices,
    AccountServices,
    PaymentMethodServices,
    ProductPurchaseOrderServices,
    ProductServices,
    ProviderServices,
    PurchaseOrderServices,
    TableServices,
    UserServices,
)
from app.services.cashier_service import CashierServices
from app.services.helper import (
    create_fake_account,
    create_fake_account_product,
    create_fake_cashier,
    create_fake_payment_methods,
    create_fake_product,
    create_fake_product_purchase_order,
    create_fake_provider,
    create_fake_purchase_order,
    create_fake_tables,
    create_fake_user,
)
from flask import Flask
from flask.cli import AppGroup


def cli_user(app: Flask):
    cli_group_user = AppGroup('user')
    session = app.db.session

    @cli_group_user.command('create')
    @click.argument('amount')
    def cli_user_create(amount: int):
        for user in range(int(amount)):
            user_data = create_fake_user(int(amount))
            UserServices.create_user(user_data)

        click.echo('New users created')

    app.cli.add_command(cli_group_user)


def cli_product(app: Flask):
    cli_group_product = AppGroup('product')
    session = app.db.session

    @cli_group_product.command('create')
    @click.argument('amount')
    def cli_product_create(amount: int):
        for user in range(int(amount)):
            product_data = create_fake_product(int(amount))
            ProductServices.create_product(product_data)

        click.echo('New products created')

    app.cli.add_command(cli_group_product)


def cli_provider(app: Flask):
    cli_group_provider = AppGroup('provider')
    session = app.db.session

    @cli_group_provider.command('create')
    @click.argument('amount')
    def cli_provider(amount: int):
        for user in range(int(amount)):
            provider_data = create_fake_provider(int(amount))
            ProviderServices.create_provider(provider_data)

        click.echo('New providers created')

    app.cli.add_command(cli_group_provider)


def cli_purchase_order(app: Flask):
    cli_group_purchase_order = AppGroup('order')
    session = app.db.session

    @cli_group_purchase_order.command('create')
    @click.argument('amount')
    def cli_purchase_order(amount: int):
        for user in range(int(amount)):
            purchase_order_data = create_fake_purchase_order(int(amount))
            purchase_order_service_retrieved_data = (
                PurchaseOrderServices.create_purchase_order(purchase_order_data)
            )

            product_purchase_order_data = create_fake_product_purchase_order(
                purchase_order_service_retrieved_data
            )
            ProductPurchaseOrderServices.create_product_purchase_order(
                product_purchase_order_data
            )
            # import ipdb

            # ipdb.set_trace()

        click.echo('Purchase order made')

    app.cli.add_command(cli_group_purchase_order)


def cli_account(app: Flask):
    cli_group_account = AppGroup('account')
    session = app.db.session

    @cli_group_account.command('create')
    @click.argument('amount')
    def cli_account(amount: int):
        for user in range(int(amount)):
            cashier_data = create_fake_cashier()
            # import ipdb

            # ipdb.set_trace()
            if cashier_data:
                CashierServices.create_cashier(cashier_data)

            if create_fake_tables():
                for table in range(5):
                    tables_data = create_fake_tables()
                    if tables_data:
                        TableServices.create_table(tables_data)

            pay_mathods_data = create_fake_payment_methods()
            if pay_mathods_data:
                PaymentMethodServices.create_payment_method(pay_mathods_data)

            account_data = create_fake_account(int(amount))
            account_service_retrieved_data = AccountServices.create_account(
                account_data
            )

            for account_product in range(5):
                account_product_data = create_fake_account_product(
                    account_service_retrieved_data
                )
                AccountProductServices.create_account_product(account_product_data)

        click.echo('New accounts opened')

    app.cli.add_command(cli_group_account)


def init_app(app: Flask):
    cli_user(app)
    cli_product(app)
    cli_provider(app)
    cli_purchase_order(app)
    cli_account(app)
