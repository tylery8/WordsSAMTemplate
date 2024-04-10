from abc import ABC
from typing import Optional, Type, TypeVar

from requests import request

from models.utils import ResponseModel
from common import Loggers

T = TypeVar("T", bound=ResponseModel)


@Loggers.auto_log
class HttpClient(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method: str, uri: str, model_class: Type[T], **kwargs) -> Optional[T]:
        try:
            data = request(method, f'{self.base_url}{uri}', **kwargs).json()
            return model_class.from_response(data)
        except:
            return None
