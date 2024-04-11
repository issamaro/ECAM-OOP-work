# import requests
from bd import BD
from article import Article
import databasestorage
import research

OPENLIBRARY_ENDPOINT = "https://openlibrary.org/search.json"

class Main:
    FILENAME = "bd.json"

    def main():

        def afficher_liste_bd(liste_article_bd):
            str_liste = ""
            for i, article in enumerate(liste_article_bd, 1):
                str_liste += f"{'-' * 20} Article {i} {'-' * 20}\n"
                str_liste += str(article) + "\n\n"
            print(str_liste)

        def choisir_variable_recherche():
            print("1. Titre")
            print("2. Auteur")
            print("3. ISBN")
            print("4. Année de publication")
            print("5. Langue")
            print("6. Code barre")
            print("7. Prix")


            choix_variable = input("Votre choix: ")
            match choix_variable:
                case "1":
                    return "title"
                case "2":
                    return "auteur_name"
                case "3":
                    return "isbn"
                case "4":
                    return "first_publish_year"
                case "5":
                    return "language"
                case "6":
                    return "code_barre"
                case "7":
                    return "prix"
                case _:
                    print("Choix invalide.")
                    return None


        def afficher_menu():
            print("1. Ajouter un article")
            print("2. Afficher la liste des articles")
            print("3. Choisir un article")
            print("4. Rechercher une BD par la valeur que vous voulez")
            print("5. Modifier une BD au choix")
            print("6. Supprimer une BD au choix")
            print("7. Sauvegarder vos données")
            print("8. Quitter")

        def ajouter_article():
            # Demander à l'utilisateur les détails de la BD
            title = input("Entrez le titre de la BD: ")
            auteur_name = input("Entrez le nom de l'auteur: ")
            isbn = input("Entrez le numéro ISBN de la BD: ")

            # Vérifier si l'année de publication est un entier valide
            while True:
                first_publish_year = input("Entrez l'année de première publication de la BD: ")
                if not first_publish_year.isdigit():
                    print("\u26A0️ L'année de publication doit être un nombre entier. \u26A0️")
                else:
                    break  # Sortir de la boucle si l'année de publication est un entier valide

            language = input("Entrez la langue de la BD: ")
            code_barre = input("Entrez le code-barres de la BD: ")

            # Vérifier si le prix est un nombre valide
            while True:
                prix = input("Entrez le prix de la BD: ")
                if not prix.isdigit():
                    print("\u26A0️ Le prix doit être un nombre entier. \u26A0️")
                else:
                    break  # Sortir de la boucle si le prix est un nombre valide

            # Créer la BD
            nouvel_article = BD(title, auteur_name, isbn, first_publish_year, language, code_barre, prix)
            Article.articles["bd"].append(nouvel_article)
            print("\n \U0001F44D BD ajouté avec succès. \U0001F44D \n")
            databasestorage.sauvegarder_article()

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
                    return None
            except ValueError:
                print("Choix invalide. Veuillez saisir un nombre.")
                return None

            # Renvoyer l'article choisi
            print(Article.articles["bd"][choix - 1])
            print("\n")
            return Article.articles["bd"][choix - 1]

        def rechercher_bd_par_titre():
            print("Choisissez la variable par laquelle vous souhaitez rechercher:")
            variable = choisir_variable_recherche()
            if variable is None:
                return  # Sortir de la fonction si le choix est invalide

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

        def modifier_article():
            article = choisir_article()  # Permet à l'utilisateur de choisir l'article à modifier
            # Si aucun article n'est choisi, sortir de la fonction
            if article is None:
                return

            print("Choisissez la variable par laquelle vous souhaitez faire une modification:")

            choix_variable = choisir_variable_recherche()  # Permet à l'utilisateur de choisir la variable à modifier
            if choix_variable is None:
                return  # Sortir de la fonction si le choix est invalide

            while True:
                valeur_modification = input(f"Entrez la valeur pour la modification par {choix_variable}: ")

                if choix_variable in ["first_publish_year", "prix"]:
                    if not valeur_modification.isdigit():
                        print("\u26A0️ L'année de publication et le prix doivent être des nombres entiers. \u26A0️")
                        continue  # Recommencer la boucle pour demander à nouveau la saisie
                break  # Sortir de la boucle si l'année de publication ou le prix est un nombre entier valide

            # Modifier l'article sélectionné en fonction de la variable choisie
            setattr(article, choix_variable, valeur_modification)
            print("Modification effectuée avec succès.")

        def supprimer_article():
            article = choisir_article()  # Permet à l'utilisateur de choisir l'article à supprimer
            # Si aucun article n'est choisi, sortir de la fonction
            if article is None:
                return

            # Demander à l'utilisateur de confirmer la suppression
            confirmation = input(f"Êtes-vous sûr de vouloir supprimer l'article {article.title}? (O/N) ").upper()

            if confirmation == "O":
                # Supprimer l'article de la liste
                Article.articles["bd"].remove(article)
                print(f"L'article {article.title} a été supprimé avec succès.")
            elif confirmation == "N":
                print("Suppression annulée.")
            else:
                print("Entrée invalide. Suppression annulée.")

        def executer():
            while True:
                afficher_menu()
                choix = input("Faites votre choix: ")
                match choix:
                    case "1":
                        ajouter_article()
                    case "2":
                        afficher_liste_bd(Article.articles["bd"])
                    case "3":
                        choisir_article()
                    case "4":
                        rechercher_bd_par_titre()
                    case "5":
                        modifier_article()
                    case "6":
                        supprimer_article()
                    case "7":
                        databasestorage.sauvegarder_article()
                    case "8":
                        databasestorage.sauvegarder_article()
                        print("Au revoir!")
                        break
                    case _:
                        print("Choix invalide. Veuillez choisir une option valide.")

        ########## pour le test ########## 
        # liste_article = Article.articles

        # Create a BD object
        # book = BD("The Catcher in the Rye", "J.D. Salinger", "9782253105677", 1951, "English", "PG123456789", 20)
        # book1 = BD("AAAAAAAA", "a", "1234567891234", 6666, "Chiinois", "CD123456789", 1000)

        # Convert the book object to a string
        # print(book)
        # liste_article["bd"].append(book)
        # liste_article["bd"].append(book1)
        # print(afficher_liste_bd())
        #####

        # charger les donnees dans le fichier bd.json
        databasestorage.charger_articles()
        executer()

    if __name__ == "__main__":
        main()