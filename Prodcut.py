class Product:
    def __init__(self,name,description,price,categories,ingredients):
        self.__name=name
        self.__description=description
        self.__price =price
        self.__categories=categories
        self.__ingredients=ingredients

    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description
    def getPrice(self):
        return self.__price
    def getCategories(self):
        return self.__categories
    def getIngredients(self):
        return self.__ingredients


    def setName(self,var):
        self.__name=var
    def setDescription(self,var):
        self.__description=var
    def setPrice(self,var):
        self.__price=var
    def setCategories(self,var):
        self.__categories = var
    def setIngredients(self,var):
        self.__ingredients=var
