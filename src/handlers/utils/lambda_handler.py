import json
from typing import Optional, Dict, Any, Type

from errors import BaseError
from models.utils import EventModel
from common import Loggers


@Loggers.auto_log
class LambdaHandler:
    def __init__(self, controller):
        self.controller = controller

    def handle_event(self, func_name: str, event_model: Type[EventModel], event: Dict[str, Any]) -> Dict[str, Any]:
        try:
            body: Optional[str] = getattr(self.controller, func_name)(event_model.from_event(event))
            return {
                'statusCode': 200,
                'body': body if body else '{}'
            }
        except BaseError as e:
            return {
                'statusCode': e.status_code,
                'body': json.dumps({'message': str(e)})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': str(e)})
            }
