from .base_error import BaseError


class InternalServerError(BaseError):
    def __init__(self, message: str = 'Internal server error'):
        super().__init__(status_code=500, message=message)
