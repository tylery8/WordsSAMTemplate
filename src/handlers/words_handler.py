from controllers import WordsController
from handlers.utils import LambdaHandler
from models.aws import ApiGatewayEvent

words_handler = LambdaHandler(WordsController())


def create_word_handler(event, context):
    return words_handler.handle_event('create_word', ApiGatewayEvent, event)


def get_word_handler(event, context):
    return words_handler.handle_event('get_word', ApiGatewayEvent, event)


def delete_word_handler(event, context):
    return words_handler.handle_event('delete_word', ApiGatewayEvent, event)
