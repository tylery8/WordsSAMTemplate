import pytest
from unittest.mock import MagicMock, patch
from models.domain import Word
from services.words_service import WordsService
from models.randomword.actions import GetRandomWordResponse, GetRandomWordRequest


@pytest.fixture
def words_table_mock():
    return MagicMock()


@pytest.fixture
def random_word_accessor_mock():
    return MagicMock()


@pytest.fixture
def words_service(words_table_mock, random_word_accessor_mock):
    words_service = WordsService()
    words_service.words_table = words_table_mock
    words_service.random_word_accessor = random_word_accessor_mock
    return words_service


def test_create_word(words_service, words_table_mock):
    with patch.object(Word, 'generate_id', return_value='123'):
        words_table_mock.put.return_value = Word(id='123', word='test')
        result = words_service.create_word('test')
        assert result == Word(id='123', word='test')
        words_table_mock.put.assert_called_once_with(item=Word(id='123', word='test'))


def test_create_random_word(words_service, random_word_accessor_mock, words_table_mock):
    with patch.object(Word, 'generate_id', return_value='123'):
        random_word_accessor_mock.get_random_word.return_value = GetRandomWordResponse(word='random_word')
        words_table_mock.put.return_value = Word(id='123', word='random_word')
        result = words_service.create_random_word()
        assert result == Word(id='123', word='random_word')
        random_word_accessor_mock.get_random_word.assert_called_once_with(GetRandomWordRequest(length=None))
        words_table_mock.put.assert_called_once_with(item=Word(id='123', word='random_word'))


def test_get_word(words_service, words_table_mock):
    words_table_mock.get.return_value = Word(id='123', word='test')
    result = words_service.get_word('123')
    assert result == Word(id='123', word='test')
    words_table_mock.get.assert_called_once_with(id='123')


def test_delete_word(words_service, words_table_mock):
    words_table_mock.delete.return_value = Word(id='123', word='deleted_word')
    result = words_service.delete_word('123')
    assert result == Word(id='123', word='deleted_word')
    words_table_mock.delete.assert_called_once_with(id='123')
