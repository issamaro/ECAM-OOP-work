# import requests
import textwrap
from bd import BD
from article import Article


class Main:
    def main():
        def afficher_liste_bd():
            str_liste = ""
            for i, article in enumerate(Article.articles["bd"], 1):
                str_liste += f"{'-' * 20} Article {i} {'-' * 20}\n"
                str_liste += str(article) + "\n\n"
            print(str_liste)

        def afficher_menu():
            print("1. Ajouter un article")
            print("2. Afficher la liste des articles")
            print("3. Choisir un article")
            print("4. Quitter")

        def ajouter_article():
            # Demander à l'utilisateur les détails de la BD
            title = input("Entrez le titre de la BD: ")
            auteur_name = input("Entrez le nom de l'auteur: ")
            isbn = input("Entrez le numéro ISBN de la BD: ")
            first_publish_year = input("Entrez l'année de première publication de la BD: ")
            language = input("Entrez la langue de la BD: ")
            code_barre = input("Entrez le code-barres de la BD: ")
            prix = input("Entrez le prix de la BD: ")

            # Créer la BD
            nouvel_article = BD(title, auteur_name, isbn, first_publish_year, language, code_barre, prix)
            Article.articles["bd"].append(nouvel_article)
            print("BD ajouté avec succès.")

        def choisir_article():
            # Afficher la liste des articles
            afficher_liste_bd()

            # Demander à l'utilisateur de choisir un article par son numéro
            choix = input("Choisissez un article par son numéro: ")

            # Vérifier si le choix est valide
            try:
                choix = int(choix)
                if choix < 1 or choix > len(Article.articles["bd"]):
                    print("Choix invalide. Veuillez choisir un numéro valide.")
                    return
            except ValueError:
                print("Choix invalide. Veuillez saisir un nombre.")
                return

            # Afficher l'article choisi
            article_choisi = Article.articles["bd"][choix - 1]
            print("Article choisi :")
            print(article_choisi)

        def executer():
            while True:
                afficher_menu()
                choix = input("Faites votre choix: ")
                if choix == "1":
                    ajouter_article()
                elif choix == "2":
                    afficher_liste_bd()
                elif choix == "3":
                    choisir_article()
                elif choix == "4":
                    print("Au revoir!")
                    break
                else:
                    print("Choix invalide. Veuillez choisir une option valide.")

                    ###### pour le test

        liste_article = Article.articles

        # Create a BD object
        book = BD("The Catcher in the Rye", "J.D. Salinger", "9782253105677", 1951, "English", 123456789, 20.0)
        book1 = BD("AAAAAAAA", "a", "1234567891234", 6666, "Chiinois", 123456789, 1000)

        # Convert the book object to a string
        # print(book)
        liste_article["bd"].append(book)
        liste_article["bd"].append(book1)
        # print(afficher_liste_bd())
        #####

        executer()

    if __name__ == "__main__":
        main()
