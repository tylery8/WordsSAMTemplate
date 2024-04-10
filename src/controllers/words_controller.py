from typing import Optional

from errors import WordNotFoundError
from models.aws import ApiGatewayEvent
from models.domain import Word
from models.domain.actions import (
    CreateWordInput, CreateWordOutput,
    GetWordInput, GetWordOutput,
    DeleteWordInput, DeleteWordOutput
)
from services import WordsService
from common import Loggers


@Loggers.auto_log
class WordsController:
    def __init__(self):
        self.service = WordsService()

    def create_word(self, event: ApiGatewayEvent):
        input: CreateWordInput = CreateWordInput.from_event(event)
        if input.word:
            # Create the given word
            word: Optional[Word] = self.service.create_word(input.word)
        else:
            # Create a random word
            word: Optional[Word] = self.service.create_random_word(input.length)
        output: Optional[CreateWordOutput] = CreateWordOutput.from_word(word) if word else None
        return output.to_output() if output else None

    def get_word(self, event: ApiGatewayEvent):
        input: GetWordInput = GetWordInput.from_event(event)
        word: Optional[Word] = self.service.get_word(input.id)
        if word is None:
            raise WordNotFoundError(word_id=input.id)
        output: Optional[GetWordOutput] = GetWordOutput.from_word(word) if word else None
        return output.to_output() if output else None

    def delete_word(self, event: ApiGatewayEvent):
        input: DeleteWordInput = DeleteWordInput.from_event(event)
        word: Optional[Word] = self.service.delete_word(input.id)
        output: Optional[DeleteWordOutput] = DeleteWordOutput.from_word(word) if word else None
        return output.to_output() if output else None
