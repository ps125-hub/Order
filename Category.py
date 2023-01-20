class Category:
    def __init__(self,name,descripcion,parent_id,products):
        self.__name = name
        self.__descripcion=descripcion
        self.__parent_id= parent_id
        self.__products=products

    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__descripcion
    def getParent_id(self):
        return self.__parent_id
    def getProducts(self):
        return self.__products

    def setName(self,var):
        self.__name=var
    def setDescription(self,var):
        self.__descripcion = var
    def setParent_id(self,var):
        self.__parent_id = var
    def setProducts(self,var):
        self.__products=var