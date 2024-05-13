import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

def test_status_code():
     response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '2292'}) 
     assert response.status_code == 200

def test_trainer_name():
     response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '2292'}) 
     assert response_name.json()["data"][0]["trainer_name"] == 'Денис'