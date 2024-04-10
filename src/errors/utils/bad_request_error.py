from .base_error import BaseError


class BadRequestError(BaseError):
    def __init__(self, message: str = 'Bad request'):
        super().__init__(status_code=400, message=message)
