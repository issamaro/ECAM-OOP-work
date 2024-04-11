from typing import Dict, List


class Article:
    articles: Dict[str, List[object]] = {
        "bd": [],
        "toys": []
    }

    def __init__(self, code_barre: str, prix: int, stock: int = 1) -> None:
        self.__prix: int = prix
        self.__stock: int = stock
        self.__code_barre: str = code_barre

    @property
    def getPrix(self) -> int:
        return self.__prix


    @property
    def getStock(self) -> int:
        return self.__stock


    @property
    def getCode_barre(self) -> str:
        return self.__code_barre

    def __str__(self) -> str:
        str_liste = ""
        for categorie, articles in Article.articles.items():
            str_liste += f"{categorie.capitalize()}:\n"
            for article in articles:
                str_liste += str(article) + "\n"
        return str_liste
