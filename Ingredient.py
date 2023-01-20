class Ingredient:
    def __init__(self,name,allergen,cometari,products):
        self.__name=name
        self.__allergen=allergen
        self.__comentari=cometari
        self.__products=products

    def getName(self):
        return self.__name
    def getAllergen(self):
        return self.__allergen
    def getCometari(self):
        return self.__comentari
    def getProducts(self):
        return self.__products

    def setName(self,var):
        self.__name=var
    def setAllergen(self,var):
        self.__allergen=var
    def setCometari(self,var):
        self.__comentari = var
    def setProducts(self,var):
        self.__products=var
    
    

