# import requests
from bd import BD
from article import Article


class Main:
    def main():
        def afficher_liste_bd(list_article_bd):
            str_liste = ""
            for i, article in enumerate(list_article_bd, 1):
                str_liste += f"{'-' * 20} Article {i} {'-' * 20}\n"
                str_liste += str(article) + "\n\n"
            print(str_liste)

        def afficher_menu():
            print("1. Ajouter un article")
            print("2. Afficher la liste des articles")
            print("4. Rechercher une BD par titre")
            print("5. Quitter")

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
            afficher_liste_bd(Article.articles["bd"])

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

        def rechercher_bd_par_titre():
            print("Choisissez la variable par laquelle vous souhaitez rechercher:")
            print("1. Titre")
            print("2. Auteur")
            print("3. ISBN")
            print("4. Année de publication")
            print("5. Langue")
            print("6. Code barre")
            print("7. Prix")
            choix_variable = input("Votre choix: ")

            if choix_variable == "1":
                variable = "title"
            elif choix_variable == "2":
                variable = "auteur_name"
            elif choix_variable == "3":
                variable = "isbn"
            elif choix_variable == "4":
                variable = "first_publish_year"
            elif choix_variable == "5":
                variable = "language"
            elif choix_variable == "6":
                variable = "code_barre"
            elif choix_variable == "7":
                variable = "prix"
            else:
                print("Choix invalide.")
                return

            valeur_recherche = input(f"Entrez la valeur pour la recherche par {variable}: ")

            # Liste pour stocker les BD correspondant au titre de recherche
            bds_trouves = []
            # Parcourir toutes les BD dans le dictionnaire d'articles
            for article in Article.articles["bd"]:

                # Si on recherche par prix ou ISBN, on utilise une comparaison directe
                if variable in ["prix", "isbn"]:
                    attribut = getattr(article, variable)()  # Appel de la méthode pour obtenir la valeur de l'attribut
                    if attribut == int(valeur_recherche):
                        bds_trouves.append(article)
                else:
                    attribut = getattr(article, variable)
                    # Sinon, on convertit l'attribut en chaîne pour effectuer la comparaison
                    if str(attribut) == valeur_recherche:
                        bds_trouves.append(article)

            # Afficher les BD trouvées
            if bds_trouves:
                print(f"\nBD(s) trouvée(s) avec comme {variable} : {valeur_recherche}\n")
                afficher_liste_bd(bds_trouves)
            else:
                print(f"Aucune BD trouvée avec comme {variable} : {valeur_recherche}")

        def executer():
            while True:
                afficher_menu()
                choix = input("Faites votre choix: ")
                if choix == "1":
                    ajouter_article()
                elif choix == "2":
                    afficher_liste_bd(Article.articles["bd"])
                elif choix == "3":
                    choisir_article()
                elif choix == "4":
                    rechercher_bd_par_titre()
                elif choix == "5":
                    print("Au revoir!")
                    break
                else:
                    print("Choix invalide. Veuillez choisir une option valide.")

        ###### pour le test
        liste_article = Article.articles

        # Create a BD object
        book = BD("The Catcher in the Rye", "J.D. Salinger", "9782253105677", 1951, "English", "PG123456789", 20)
        book1 = BD("AAAAAAAA", "a", "1234567891234", 6666, "Chiinois", "CD123456789", 1000)

        # Convert the book object to a string
        # print(book)
        liste_article["bd"].append(book)
        liste_article["bd"].append(book1)
        # print(afficher_liste_bd())
        #####

        executer()

    if __name__ == "__main__":
        main()
