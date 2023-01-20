class LineProduct:
    def __init__(self,order_id,product_id,quantity,price):
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__price = price
    
    def getOrderID(self):
        return self.__order_id
    def getProductID(self):
        return self.__product_id
    def getQuantity(self):
        return self.__quantity
    def getPrice(self):
        return self.__price

    def setOrderID(self,var):
        self.__order_id=var
    def setProductID(self,var):
        self.__product_id=var
    def setQuantity(self,var):
        self.__quantity=var
    def setPrice(self,var):
        self.__price=var