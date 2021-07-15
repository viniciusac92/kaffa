from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    # importar as models aqui embaixo
    from app.models.product_model import ProductModel
    from app.models.operator_model import OperatorModel
    from app.models.cashier_model import CashierModel
    from app.models.operator_cashier_model import OperatorCashierModel
    from app.models.table_model import TableModel
    from app.models.waiter_model import WaiterModel
    from app.models.account_model import AccountModel
    from app.models.account_product import AccountProductModel
    from app.models.stock_product import StockProductModel
    from app.models.payment_method_model import PaymentMethodModel
    from app.models.manager_model import ManagerModel
    from app.models.account_product import AccountProductModel
    from app.models.stock_product import StockProductModel
    from app.models.provider_model import ProviderModel
    from app.models.provider_product_model import ProviderProductModel
    from app.models.purchase_order_model import PurchaseOrderModel
    from app.models.product_purchase_order_model import ProductPurchaseOrderModel
    from app.models.product_model import ProductModel
    from app.models.user_model import UserModel
