from http import HTTPStatus

class UniqueKeyError(Exception):
    def __init__(self, key_list: list) -> None:
        self.message = (
            {"error":{
                "message": f'the following keys has to be unique: {key_list}.'
            }},
            HTTPStatus.BAD_REQUEST
        )
        super().__init__(self.message)
