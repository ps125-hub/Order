class Order:
    def __init__(self,table,client,pax,waiter,priceTotal,lineProducts,state):
        self.__table = table
        self.__client = client
        self.__pax = pax
        self.__waiter = waiter
        self.__priceTotal = priceTotal
        self.__lineProducts = lineProducts
        self.__state= state

    def getTable(self):
        return self.__table
    def getClient(self):
        return self.__client
    def getPax(self):
        return self.__pax
    def getWaiter(self):
        return self.__waiter
    def getPriceTotal(self):
        return self.__priceTotal
    def getLineProducts(self):
        return self.__lineProducts
    def getState(self):
        return self.__state

    def setTable(self,var):
        self.__table=var
    def setClient(self,var):
        self.__client=var
    def setPax(self,var):
        self.__pax=var
    def setWaiter(self,var):
        self.__waiter=var
    def setPriceTotal(self,var):
        self.__priceTotal=var
    def setLineProducts(self,var):
        self.__lineProducts=var
    def setState(self,var):
        self.__state=var

