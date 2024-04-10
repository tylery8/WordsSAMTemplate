import pytest
from pydantic import ValidationError

from models.domain import Word
from models.domain.actions import CreateWordInput, CreateWordOutput


@pytest.mark.parametrize(
    "word, length, expected_error",
    [
        ("hello", 5, None),
        (None, 5, None),
        ("hello", None, None),
        (None, None, None),
        ("", None, ValidationError),
        ("hi", 6, ValidationError),
        (None, 21, ValidationError),
        (None, 2, ValidationError),
        ("hello", 6, ValidationError),
    ],
)
def test_create_word_input_validation(word, length, expected_error):
    if expected_error is None:
        assert CreateWordInput(word=word, length=length)
    else:
        with pytest.raises(expected_error):
            CreateWordInput(word=word, length=length)


@pytest.mark.parametrize(
    "word, expected",
    [
        (Word(id='101', word='hey'), CreateWordOutput(id='101', word='hey')),
        (Word(id='123', word='hello'), CreateWordOutput(id='123', word='hello')),
    ],
)
def test_create_word_output_from_word(word, expected):
    assert CreateWordOutput.from_word(word) == expected
