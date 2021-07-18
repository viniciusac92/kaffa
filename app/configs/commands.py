import click
from app.services.helper import create_fake_user
from app.services.user_service import UserServices
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
            # import ipdb

            # ipdb.set_trace()
            UserServices.create_user(user_data)

            click.echo('OK')

    app.cli.add_command(cli_group_user)


# def cli_product(app: Flask):
#     cli_group_product = AppGroup('product')
#     session = app.db.session

#     @cli_group_product.command('create')
#     @click.argument('amount')
#     def cli_product_create(amount: int):
#         # create

#         click.echo('New products created')


# def cli_provider(app: Flask):
#     @click.argument('amount')
#     def cli_provider(amount: int):
#         # create

#         click.echo('New providers created')


# def cli_purchase_order(app: Flask):
#     @click.argument('amount')
#     def cli_purchase_order(amount: int):
#         # create

#         click.echo('Purchase order made')


# def cli_account(app: Flask):
#     @click.argument('amount')
#     def cli_account(amount: int):

#         click.echo('New accounts opened')


def init_app(app: Flask):
    cli_user(app)
    # cli_product(app)
    # cli_provider(app)
    # cli_account(app)
