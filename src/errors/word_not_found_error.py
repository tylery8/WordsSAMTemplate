from typing import Optional

from .utils.not_found_error import NotFoundError


class WordNotFoundError(NotFoundError):
    def __init__(self, word_id: Optional[str] = None):
        missing = f'Word {word_id}' if word_id else 'Word'
        super().__init__(missing=missing)
