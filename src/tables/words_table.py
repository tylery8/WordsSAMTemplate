from models.domain import Word
from tables.utils import DynamoDBTable
from common import Config, Loggers


@Loggers.auto_log
class WordsTable(DynamoDBTable):
    def __init__(self):
        super().__init__(Config.WORDS_TABLE_NAME, Word)
