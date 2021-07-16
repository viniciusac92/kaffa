from http import HTTPStatus

class PurchaseClosedError(Exception):
    def __init__(self) -> None:
        self.message = (
            {"error":{
                "message": "cannot include new products in a finished purchase",
            }},
            HTTPStatus.BAD_REQUEST
        )
        super().__init__(self.message)
