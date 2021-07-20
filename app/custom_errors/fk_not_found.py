from http import HTTPStatus

class FkNotFoundError(Exception):
    def __init__(self, text: str) -> None:
        self.message = (
            {"error": f"register {text} not found."},
            HTTPStatus.NOT_FOUND
        )
        super().__init__(self.message)