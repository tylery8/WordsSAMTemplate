import pytest
from pydantic import ValidationError

from models.domain import Word
from models.domain.actions import GetWordInput, GetWordOutput


@pytest.mark.parametrize(
    "word_id, expected_error",
    [
        ("101", None),
        ("", ValidationError),
        (None, ValidationError),
    ],
)
def test_get_word_input_validation(word_id, expected_error):
    if expected_error is None:
        assert GetWordInput(id=word_id)
    else:
        with pytest.raises(expected_error):
            GetWordInput(id=word_id)


@pytest.mark.parametrize(
    "word, expected",
    [
        (Word(id='101', word='hey'), GetWordOutput(id='101', word='hey')),
        (Word(id='123', word='hello'), GetWordOutput(id='123', word='hello')),
    ],
)
def test_get_word_output_from_word(word, expected):
    assert GetWordOutput.from_word(word) == expected
