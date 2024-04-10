from abc import ABC
from typing import Type, Optional, TypeVar, Generic

import boto3

from models.aws import DynamoDBItem
from common import Loggers

dynamodb = boto3.resource('dynamodb')
T = TypeVar('T', bound=DynamoDBItem)


@Loggers.auto_log
class DynamoDBTable(Generic[T], ABC):
    def __init__(self, table_name: str, item_class: Type[T]):
        self.item_class = item_class
        self.table = dynamodb.Table(table_name) if table_name else None

    def put(self, item: T) -> Optional[T]:
        self.table.put_item(Item=item.to_ddb())
        return item

    def get(self, **key) -> Optional[T]:
        ddb_item = self.table.get_item(Key=key).get('Item')
        return self.item_class.from_ddb(ddb_item) if ddb_item else None

    def delete(self, **key) -> Optional[T]:
        ddb_item = self.table.delete_item(Key=key, ReturnValues='ALL_OLD').get('Attributes')
        return self.item_class.from_ddb(ddb_item) if ddb_item else None
