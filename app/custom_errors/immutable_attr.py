from http import HTTPStatus

class ImmutableAttrError(Exception):
    def __init__(self, text: str) -> None:
        self.message = (
            {"error": f"cannot edit {text}."},
            HTTPStatus.NOT_FOUND
        )
        super().__init__(self.message)