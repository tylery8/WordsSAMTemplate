from typing import Optional

from accessors import RandomWordAccessor
from models.domain import Word
from models.randomword.actions import GetRandomWordResponse, GetRandomWordRequest
from tables import WordsTable
from common import Loggers


@Loggers.auto_log
class WordsService:
    def __init__(self):
        self.words_table = WordsTable()
        self.random_word_accessor = RandomWordAccessor()

    def create_word(self, word_str: str) -> Optional[Word]:
        word: Optional[Word] = Word(id=Word.generate_id(), word=word_str)
        word: Optional[Word] = self.words_table.put(item=word) if word else None
        return word

    def create_random_word(self, length: Optional[int] = None) -> Optional[Word]:
        request: GetRandomWordRequest = GetRandomWordRequest(length=length)
        response: Optional[GetRandomWordResponse] = self.random_word_accessor.get_random_word(request)
        return self.create_word(response.word) if response else None

    def get_word(self, word_id: str) -> Optional[Word]:
        word: Optional[Word] = self.words_table.get(id=word_id)
        return word

    def delete_word(self, word_id: str) -> Optional[Word]:
        word: Optional[Word] = self.words_table.delete(id=word_id)
        return word if word else None
