import json
from decimal import Decimal
from typing import TypeVar, Any, Dict, Optional, Type

from models.utils import ItemModel

T = TypeVar('T', bound='DynamoDBItem')


class DynamoDBItem(ItemModel):
    def to_ddb(self) -> Dict[str, Any]:
        return json.loads(json.dumps(self.to_item()), parse_float=Decimal)

    @classmethod
    def from_ddb(cls: Type[T], item: Dict[str, Any]) -> Optional[T]:
        return cls.from_item(item)
