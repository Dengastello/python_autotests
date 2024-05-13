import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo": "generate"
}

body_change = {
    "pokemon_id": "27080",
    "name": "generate",
    "photo": "generate"
}

body_add = {
    "pokemon_id": "27080"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)