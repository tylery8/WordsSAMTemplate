from .base_error import BaseError


class NotFoundError(BaseError):
    def __init__(self, missing: str = 'Item'):
        message = f"{missing} not found"
        super().__init__(status_code=404, message=message)
