#extract.py

from src.extract import extract_description_effect

import time

# Transformation de données, on ajoute la description de chaque abilité
def transform_ability_pokemon_by_description(data_pokemons):
    for pokemon in data_pokemons:
        for ability in pokemon["abilities"]:
            url = ability["url"]
            ability_description = extract_description_effect(url)
            #Ajout de la description dans ability
            ability["description"] = ability_description.get("effect")
            time.sleep(1)
    time.sleep(1)
    return data_pokemons



