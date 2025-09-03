#extract.py

import requests
import time

# Fonctions d'extraction de données

#Fonction simple pour effectuer une requête GET et retourner le JSON.
def extract (url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erreurs lors de l'appel à l'API : {e}")
        return {}

#Extrait les détails d’un Pokémon (à partir de son URL) : capacités, types, taille, poids, etc
def extract_pokemon_details_limit (pokemon):
    details_pokemon = extract(pokemon["url"])
    abilities = [
        {
            "name": ability["ability"]["name"],
            "url": ability["ability"]["url"],
            "is_hidden": ability["is_hidden"],
            "slot": ability["slot"]
        }
        for ability in details_pokemon["abilities"]
    ]

    types = [
        {
            "slot": type_pokemon["slot"],
            "name": type_pokemon["type"]["name"] 
        }
        for type_pokemon in details_pokemon["types"]
    ]

    data_pokemon = {
        "pokemon_name": pokemon["name"],
        "abilities": abilities,
        "types": types,
        "base_experience": details_pokemon["base_experience"],
        "height": details_pokemon["height"],
        "weight": details_pokemon["weight"]
    }
    return data_pokemon

#Extrait la description de l’effet d’une capacité en anglais
def extract_description_effect(url_ability):
    response_description = {"url": url_ability, "effect": None}
    my_ability = extract(url_ability)
    for entry in my_ability["effect_entries"]:
        if entry["language"]["name"] == "en":
            #response_description[url_ability] = {entry["effect"]}, dictionnaire plutot qu'un set
            #response_description[url_ability] = entry["effect"]
            response_description = {"url": url_ability, "effect": entry["effect"]}            
    return response_description

#Extrait une liste de Pokémon (limités par le paramètre dans l'URL) et leurs détails respectifs
def extract_pokemons_and_details(url_pokemons):
    my_data = extract(url_pokemons)
    data_pokemon_100_details = []
    
    for pokemon  in my_data["results"]:   
        data_pokemon = extract_pokemon_details_limit(pokemon)
        data_pokemon_100_details.append(data_pokemon)
        time.sleep(1)
    return data_pokemon_100_details

#Extrait la liste de capacités et leurs descriptions
def extract_description_abilities(url_abilities):
    descriptions_abilities = []
    data_abilities_response = extract(url_abilities)
    for ability in data_abilities_response["results"]:
        descriptions_abilities.append(extract_description_effect(ability["url"]))
        time.sleep(1)
    return descriptions_abilities


