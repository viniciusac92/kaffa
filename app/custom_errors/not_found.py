from http import HTTPStatus

class NotFoundError(Exception):
    def __init__(self) -> None:
        self.message = (
            {"error": "register not found."},
            HTTPStatus.NOT_FOUND
        )
        super().__init__(self.message)