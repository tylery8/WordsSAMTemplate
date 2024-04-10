import json
from typing import Optional, Dict, Any

from models.utils import EventModel


class ApiGatewayEvent(EventModel):
    pathParameters: Optional[Dict[str, Any]]
    queryStringParameters: Optional[Dict[str, Any]]
    body: Optional[str]

    def get_input_args(self):
        try:
            body_data = json.loads(self.body or "{}")
        except json.JSONDecodeError:
            body_data = {}
        return {
            **(self.queryStringParameters or {}),
            **body_data,
            **(self.pathParameters or {}),
        }
