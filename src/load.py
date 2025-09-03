#load.py

import json
import pandas as pd

# Exportation des données transformés dans un fichier JSON
def save_json_format(data_pokemons, filename="pokemons_details_and_abilities.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_pokemons, f, indent=4, ensure_ascii=False)
    print(f" Les données ont été enregistrées dans le fichier {filename}")



#Exportation des données dans un fichier CSV
def save_csv_format(data_pokemons, filename="pokemons_details_and_abilities.csv"):
    flat_data = []
    for pokemon in data_pokemons:
        for ability in pokemon["abilities"]:
            flat_data.append({
                "pokemon_name": pokemon["pokemon_name"],
                "base_experience": pokemon["base_experience"],
                "height": pokemon["height"],
                "weight": pokemon["weight"],
                "types": " , ".join([type_name["name"] for type_name in pokemon["types"]]),
                "ability_name": ability["name"],
                "ability_url": ability["url"],
                "ability_is_hidden": ability["is_hidden"],
                "ability_slot": ability["slot"],
                "pokemon_description": ability.get("description", "") #Pour éviter les erreurs si description null
            })
    df = pd.DataFrame(flat_data)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f" Les données ont été enregistrées dans le fichier {filename}")

