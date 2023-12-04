import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', timeout=5)
    assert response.status_code == 200, 'Unexpected status code for /trainers'

def test_trainer_id():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': '3762'}, timeout=5)
    assert response.json()['trainer_name'] == 'Tonyman', 'Incorrect name'