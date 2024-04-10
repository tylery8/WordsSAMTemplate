from typing import List


class BaseError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code

    @classmethod
    def format_pydantic_errors(cls, errors: List[dict]) -> str:
        return (
            f"{len(errors)} validation error{'s' if len(errors) > 1 else ''}: " +
            " ".join(f"{error['loc'][0]} - {error['msg']}." for error in errors)
        )
