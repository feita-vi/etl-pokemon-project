#main.py

from src.extract import extract_pokemons_and_details
from src.transform import transform_ability_pokemon_by_description
from src.load import save_json_format, save_csv_format


# Liens vers les endpoints de l’API pour récupérer une liste de Pokémon ou de capacités.
LIMIT_100_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/?limit=100"
LIMIT_2_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/?limit=2"
ABILITIES_URL = "https://pokeapi.co/api/v2/ability"

def main():
    data_response_pokemons = extract_pokemons_and_details(LIMIT_100_POKEMON_URL)
    data_pokemons_transformed = transform_ability_pokemon_by_description(data_response_pokemons)
    save_json_format(data_pokemons_transformed)
    save_csv_format(data_pokemons_transformed)

if __name__ == "__main__":
    main()