import pytest

from models.randomword.actions import GetRandomWordResponse


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (['hello'], GetRandomWordResponse(word='hello')),
        (['example'], GetRandomWordResponse(word='example')),
    ]
)
def test_get_random_word_response_from_response(input_data, expected_output):
    assert GetRandomWordResponse.from_response(input_data) == expected_output
