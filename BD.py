from article import Article


class BD(Article):

    def __init__(self, title: str, auteur_name: str, isbn: str, first_publish_year: int, language: str, code_barre: str,
                 prix: float, stock: int = 1) -> None:
        super().__init__(code_barre, prix, stock)  
        self.__title: str = title
        self.__auteur_name: str = auteur_name
        self.__isbn: str = isbn
        self.__first_publish_year: str = first_publish_year
        self.__language: str = language

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def auteur_name(self):
        return self.__auteur_name

    @auteur_name.setter
    def auteur_name(self, value):
        self.__auteur_name = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def first_publish_year(self):
        return self.__first_publish_year

    @first_publish_year.setter
    def first_publish_year(self, value):
        self.__first_publish_year = value

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    def prix(self) -> float:
        return super().prix  # Appel du getter de prix de la classe parente

    def stock(self):
        return super().stock  # Appel du getter de stock de la classe parente

    def code_barre(self):
        return super().code_barre  # Appel du getter de code_barre de la classe parente


    def __str__(self) -> str:
        return f"Title: {self.title}\nAuteur: {self.auteur_name}\nISBN: {self.isbn}\nFirst Publish Year: {self.first_publish_year}\nLanguage: {self.language}\nCode Barre: {self.code_barre()}\nPrix: {self.prix()} €\nStock: {self.stock()}"
