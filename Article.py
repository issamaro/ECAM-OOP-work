from typing import Dict, List


class Article:
    articles: Dict[str, List[object]] = {
        "bd": [],
        "toys": []
    }

    def __init__(self, code_barre: str, prix: float, stock: int = 1) -> None:
        self.__prix: float = prix
        self.__stock: int = stock
        self.__code_barre: str = code_barre

    @property
    def prix(self) -> float:
        return self.__prix

    @prix.setter
    def prix(self, value: float) -> None:
        self.__prix = value

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, value: int) -> None:
        self.__stock = value

    @property
    def code_barre(self) -> str:
        return self.__code_barre

    @code_barre.setter
    def code_barre(self, value: str) -> None:
        self.__code_barre = value

    def __str__(self) -> str:
        str_liste = ""
        for categorie, articles in Article.articles.items():
            str_liste += f"{categorie.capitalize()}:\n"
            for article in articles:
                str_liste += str(article) + "\n"
        return str_liste
