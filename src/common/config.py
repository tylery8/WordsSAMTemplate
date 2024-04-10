import os


class Config:
    WORDS_TABLE_NAME = os.getenv('WORDS_TABLE_NAME', None)
    RANDOM_WORDS_BASE_URL = 'https://random-word-api.herokuapp.com'
