import requests

HOST = 'https://api.pokemonbattle.me:9104'
trainer_token = 'a0ec5189084c86f8cbd85474a21fae88'
trainer_id = '3762'

response = requests.post(url=f'{HOST}/pokemons',
                         json={
                            "name": "generate",
                            "photo": "generate"
                            },
                         headers={'Content-Type': 'application/json', 'trainer_token': trainer_token}, timeout=5)

print(response.json())

pokemon_id = response.json()['id']

response = requests.put(url=f'{HOST}/pokemons',
                         json={
                            "pokemon_id": pokemon_id,
                            "name": "generate",
                            "photo": "generate"
                            },
                         headers={'Content-Type': 'application/json', 'trainer_token': trainer_token}, timeout=5)

print(response.json()) 

response = requests.post(url=f'{HOST}/trainers/add_pokeball',
                         json={"pokemon_id": pokemon_id},
                         headers={'Content-Type': 'application/json', 'trainer_token': trainer_token}, timeout=5)

print(response.json()) 