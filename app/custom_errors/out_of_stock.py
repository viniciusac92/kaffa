from http import HTTPStatus

class OutOfStockError(Exception):
    def __init__(self, data: str) -> None:
        self.message = (
            {
                "error":f'product {data} is out of stock.',
            },
            HTTPStatus.BAD_REQUEST
        )
        super().__init__(self.message)
