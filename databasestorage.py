import json
from main import FILENAME
from article import Article
from bd import BD


def sauvegarder_article():
    data = {"bd": []}
    for bd in Article.articles["bd"]:
        bd_data = {
            "title": bd.title,
            "auteur_name": bd.auteur_name,
            "isbn": bd.isbn,
            "first_publish_year": bd.first_publish_year,
            "language": bd.language,
            "code_barre": bd.code_barre(),
            "prix": bd.prix(),
            "stock": bd.stock()
        }
        data["bd"].append(bd_data)

    # Écrire les nouvelles données dans le fichier    
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def charger_articles():
    with open(FILENAME, "r") as file:
        data = json.load(file)  # Charger les données depuis le fichier JSON

        # Si des données sont présentes
        if data:
            # Créer des objets BD à partir des données et les ajouter à la liste
            for bd_data in data.get("bd", []):
                nouvelle_bd = BD(bd_data["title"], bd_data["auteur_name"], bd_data["isbn"],
                                 bd_data["first_publish_year"], bd_data["language"], bd_data["code_barre"],
                                 bd_data["prix"], bd_data["stock"])
                Article.articles["bd"].append(nouvelle_bd)
