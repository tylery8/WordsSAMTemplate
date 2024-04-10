import json

import pytest
import requests

from utils.api_utils import get_base_url
from utils.test_data import word, missing_word_id

base_url = get_base_url('WordsSAMTemplate', 'us-west-2')


@pytest.fixture(scope="module")
def word_id(request):
    response = requests.post(
        f'{base_url}/words',
        data=json.dumps({'word': word})
    )
    body = response.json()
    word_id = body.get('id')

    assert body == {'id': word_id, 'word': word}
    assert response.status_code == 200

    yield word_id

    requests.delete(f'{base_url}/words/{word_id}')


@pytest.fixture(scope="module")
def random_word_id(request):
    response = requests.post(
        f'{base_url}/words?length=5',
    )
    body = response.json()
    random_word_id = body.get('id')

    assert len(body['word']) == 5
    assert response.status_code == 200

    yield random_word_id

    requests.delete(f'{base_url}/words/{random_word_id}')


def test_get_word(word_id):
    response = requests.get(f'{base_url}/words/{word_id}')
    body = response.json()

    assert body == {'id': word_id, 'word': word}
    assert response.status_code == 200


def test_get_random_word(random_word_id):
    response = requests.get(f'{base_url}/words/{random_word_id}')
    body = response.json()

    assert len(body['word']) == 5
    assert response.status_code == 200


def test_delete_word(word_id):
    response = requests.delete(f'{base_url}/words/{word_id}')
    body = response.json()

    assert body == {'id': word_id, 'word': word}
    assert response.status_code == 200


def test_get_no_word():
    response = requests.get(f'{base_url}/words/{missing_word_id}')
    body = response.json()

    assert 'not found' in body['message']
    assert response.status_code == 404


def test_delete_no_word():
    response = requests.delete(f'{base_url}/words/{missing_word_id}')
    body = response.json()

    assert body == {}
    assert response.status_code == 200


def test_create_invalid_word():
    response = requests.post(
        f'{base_url}/words',
        data=json.dumps({'word': '', 'length': 50})
    )
    body = response.json()

    assert '2 validation errors' in body['message']
    assert response.status_code == 400
