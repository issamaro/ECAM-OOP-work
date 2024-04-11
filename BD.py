from article import Article


class BD(Article):

    def __init__(self, title: str, auteur_name: str, isbn: str, first_publish_year: int, language: str, code_barre: str,
                 prix: int, stock: int = 1) -> None:
        super().__init__(code_barre, prix, stock)  
        self.__title: str = title
        self.__auteur_name: str = auteur_name
        self.__isbn: str = isbn
        self.__first_publish_year: str = first_publish_year
        self.__language: str = language

    @property
    def getTitle(self):
        return self.__title


    @property
    def getAuteur_name(self):
        return self.__auteur_name


    @property
    def getIsbn(self):
        return self.__isbn


    @property
    def getFirst_publish_year(self):
        return self.__first_publish_year

    @property
    def getLanguage(self):
        return self.__language

    def prix(self):
        return super().getPrix  # Appel du getter de prix de la classe parente

    def stock(self):
        return super().getStock  # Appel du getter de stock de la classe parente

    def code_barre(self):
        return super().getCode_barre  # Appel du getter de code_barre de la classe parente

    def __str__(self) -> str:
        return f"Title: {self.getTitle}\nAuteur: {self.getAuteur_name}\nISBN: {self.getIsbn}\nFirst Publish Year: {self.getFirst_publish_year}\nLanguage: {self.getLanguage}\nCode Barre: {self.code_barre()}\nPrix: {self.prix()} €\nStock: {self.stock()}"
