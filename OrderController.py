from Category import Category
from Prodcut import Product
from Ingredient import Ingredient
from Order import Order
from LineProduct import LineProduct
from OrderApi import getCategoriesAll,putLineProduct,getLineProduct,deleteLineProduct,postLineProduct,getProductsALL,getIngredientsALL,getLineProductAll,getOrderAll,putOrder,endOrder,getOrderID,deleteOrder,postOrder
class OrderController:
    def __init__(self):
        self.__Products = getProductsALL()
        self.__linesProducts = getLineProductAll()
        self.__orders = getOrderAll()

    def getProducts(self):
        self.__Products = getProductsALL()
        return self.__Products

    def getLinesProducts(self):
        self.__linesProducts = getLineProductAll()
        return self.__linesProducts

    def getLineProdut(self,idline):
        lineProduct = getLineProduct(idline)
        return lineProduct

    def getOrders(self):
        self.__orders = getOrderAll()
        return self.__orders

    def getOrder(self,idorder):
        order = getOrderID(idorder)
        return order

    def confirmOrder(self,idorder):
        endOrder(idorder)
        
    def updateOrder(self,idorder,order):
        putOrder(idorder,order)

    def updateLineProduct(self,idline,lineproduct):
        putLineProduct(idline,lineproduct)

    def delOrder(self,idorder):
        deleteOrder(idorder)

    def addOrder(self,table,client,pax,waiter,priceTotal,lineProducts,state):
        order = Order(table,client,pax,waiter,priceTotal,lineProducts,state)
        idorder = postOrder(order)
        return idorder

    def addLineProduct(self,idorder,idproduct,quantity,price):
        lineproduct = LineProduct(idorder,idproduct,quantity,price)
        postLineProduct(lineproduct)
    
    def delLineProduct(self,idline):
        deleteLineProduct(idline)