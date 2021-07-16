from http import HTTPStatus

class AccountClosedError(Exception):
    def __init__(self) -> None:
        self.message = (
            {"error":{
                "message": "cannot include new products in a closed account",
            }},
            HTTPStatus.BAD_REQUEST
        )
        super().__init__(self.message)
