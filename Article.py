from typing import Dict, List


class Article:
    articles: Dict[str, List[object]] = {
        "bd": [],
        "toys": []
    }

    def __init__(self, code_barre: str, prix: int, stock: int = 1) -> None:
        self._prix: int = prix
        self._stock: int = stock
        self._code_barre: str = code_barre

    @property
    def prix(self) -> int:
        return self._prix

    @prix.setter
    def prix(self, value: int) -> None:
        self._prix = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        self._stock = value

    @property
    def code_barre(self) -> str:
        return self._code_barre

    @code_barre.setter
    def code_barre(self, value: str) -> None:
        self._code_barre = value

    def __str__(self) -> str:
        str_liste = ""
        for categorie, articles in Article.articles.items():
            str_liste += f"{categorie.capitalize()}:\n"
            for article in articles:
                str_liste += str(article) + "\n"
        return str_liste
