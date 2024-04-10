from typing import Optional

from accessors.utils import HttpClient
from models.randomword.actions import GetRandomWordResponse, GetRandomWordRequest
from common import Config, Loggers


@Loggers.auto_log
class RandomWordAccessor(HttpClient):
    def __init__(self):
        super().__init__(Config.RANDOM_WORDS_BASE_URL)

    def get_random_word(self, request: GetRandomWordRequest) -> Optional[GetRandomWordResponse]:
        uri = '/word?' + request.to_query_string('length')
        return self.request('GET', uri, model_class=GetRandomWordResponse)
