from models.aws import DynamoDBItem


class Word(DynamoDBItem):
    id: str
    word: str
