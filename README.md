# Pokémon ETL Projetc - Extract, Transform and Load Data from PokeAPI                              


Un projet Python complet de type **ETL (Extract - Transform - Load)**, conçu pour collecter, transformer et sauvegarder des données depuis l’API officielle [PokeAPI](https://pokeapi.co/).


💡 Objectif : démontrer mes compétences en **consommation d'API REST**, **structuration de projet Python**, **traitement de données** avec `pandas`, et **gestion de code et de fichiers**. On récupère les données qui nous intéresse et on ajoute la description de chaque abilités des pokémons.


## Fonctionnalités

- 🔍 Extraction automatique de 100 Pokémon via l'API
- 🧠 Récupération et intégration des **descriptions de capacités**
- 💾 Export des données :
  - en **JSON** formaté (UTF-8)
  - en **CSV** lisible avec Excel ou Pandas
- 🧱 Architecture **ETL modulaire** : `extract`, `transform`, `load`


## Structure du projet

```
├── main.py # Script principal du pipeline ETL
├── requirements.txt # Dépendances
├── pokemons_details_and_abilities.json # Fichier JSON généré
├── pokemons_details_and_abilities.csv # Fichier CSV généré
├── /src/
│     ├── extract.py # Appel API & extraction de données
│     ├── transform.py # Enrichissement des données 
│     └── load.py # Export JSON + CSV
└── README.md
````

## Stack technique

- Langage: Python 3.13
- API: pokeAPI (https://pokeapi.co/)
- Requêtes HTTP: request
- Manipulation de données: pandas
- Format export: JSON, CSV
- Structure code: Architechture ETL(Extract/Transform/Load)
- Versionning: Git+Github


## Exemple de sortie JSON:
````
{
        "pokemon_name": "diglett",
        "abilities": [
            {
                "name": "sand-veil",
                "url": "https://pokeapi.co/api/v2/ability/8/",
                "is_hidden": false,
                "slot": 1,
                "description": "During a sandstorm, this Pokémon has 1.25× its evasion, and it does not take sandstorm damage regardless of type.\n\nThe evasion bonus does not count as a stat modifier.\n\nOverworld: If the lead Pokémon has this ability, the wild encounter rate is halved in a sandstorm."
            },
            {
                "name": "arena-trap",
                "url": "https://pokeapi.co/api/v2/ability/71/",
                "is_hidden": false,
                "slot": 2,
                "description": "While this Pokémon is in battle, opposing Pokémon cannot flee or switch out.  flying-type Pokémon and Pokémon in the air, e.g. due to levitate or magnet rise, are unaffected.\n\nPokémon with run away can still flee.  Pokémon can still switch out with the use of a move or item.\n\nOverworld: If the lead Pokémon has this ability, the wild encounter rate is doubled."
            },
            {
                "name": "sand-force",
                "url": "https://pokeapi.co/api/v2/ability/159/",
                "is_hidden": true,
                "slot": 3,
                "description": "During a sandstorm, this Pokémon's rock-, ground-, and steel-type moves have 1.3× their base power.  This Pokémon does not take sandstorm damage, regardless of type."
            }
        ],
        "types": [
            {
                "slot": 1,
                "name": "ground"
            }
        ],
        "base_experience": 53,
        "height": 2,
        "weight": 8
    }


Auteur: FEITAMA Vianelle alias FEITA-Vi
https://www.linkedin.com/in/feitamavianelle/


Ce fichier est sous licence MIT - voir le fichier LICENSE
