from abc import ABC
from typing import Dict
from urllib.parse import urlencode

from pydantic import BaseModel


class RequestModel(ABC, BaseModel):
    def to_query_string(self, *args) -> str:
        return urlencode({
            k: v
            for k, v
            in self.model_dump(mode='json').items()
            if (not args or k in args) and v is not None
        })

    def to_payload(self, *args) -> Dict:
        return {
            k: v
            for k, v
            in self.model_dump(mode='json').items()
            if (not args or k in args) and v is not None
        }
