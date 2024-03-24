from article import Article


class BD(Article):

    def __init__(self, title: str, auteur_name: str, isbn: str, first_publish_year: str, language: str, code_barre: str,
                 prix: int) -> None:
        super().__init__(code_barre, prix)
        self._title: str = title
        self._auteur_name: str = auteur_name
        self._isbn: str = isbn
        self._first_publish_year: str = first_publish_year
        self._language: str = language

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def auteur_name(self):
        return self._auteur_name

    @auteur_name.setter
    def auteur_name(self, value):
        self._auteur_name = value

    @property
    def getIsbn(self):
        return self._isbn

    @getIsbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def first_publish_year(self):
        return self._first_publish_year

    @first_publish_year.setter
    def first_publish_year(self, value):
        self._first_publish_year = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    def prix(self):
        return super().prix  # Appel du getter de prix de la classe parente

    def stock(self):
        return super().stock  # Appel du getter de stock de la classe parente

    def code_barre(self):
        return super().code_barre  # Appel du getter de code_barre de la classe parente

    def __str__(self) -> str:
        return f"Title: {self._title}\nAuteur: {self._auteur_name}\nISBN: {self._isbn}\nFirst Publish Year: {self._first_publish_year}\nLanguage: {self._language}\nCode Barre: {self._code_barre}\nPrix: {self._prix} €\nStock: {self._stock}"
