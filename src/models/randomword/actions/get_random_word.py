from typing import Optional, List

from models.utils import RequestModel, ResponseModel


class GetRandomWordRequest(RequestModel):
    length: Optional[int] = None


class GetRandomWordResponse(ResponseModel):
    word: str

    @classmethod
    def from_response(cls, obj: List[str]) -> Optional['GetRandomWordResponse']:
        return super().from_response(dict(word=obj[0]))
