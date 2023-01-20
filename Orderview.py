from OrderController import OrderController
from Category import Category
from Prodcut import Product
from Ingredient import Ingredient
controller = OrderController()

def getProducts():
    products = controller.getProducts()
    for i in range(len(products)):
        for id, product in products[i].items():
            print("Id:",id)
            print("\tName:",product.getName())
            print("\tDescription:",product.getDescription())
            print("\tPrice:",product.getPrice())
def linesProducstOrder(order):
    linesProducts = order.getLineProducts()
    for i in range(len(linesProducts)):
        id = linesProducts[i]
        lineProduct = controller.getLineProdut(id)
        print("Id:",id)
        print("\tTable:",lineProduct.getOrderID()[1])
        print("\tProduct:",lineProduct.getProductID()[1])
        print("\tQuantity:",lineProduct.getQuantity())
        print("\tPrice:",lineProduct.getPrice())  

def createOrder():
    table = int(input("Enter table: "))
    client = "table"+str(table)
    pax = int(input("Enter pax: "))
    waiter = "Administrador"
    priceTotal=0
    lineProducts = []
    state="D"
    idorder =controller.addOrder(table,client,pax,waiter,priceTotal,lineProducts,state)
    while True:
        option =input("Add a line producto?(y/n): ")
        if(option =="n"):
            break
        elif(option == "y"):
            addLineProduct(idorder)

def addLineProduct(idorder):
    getProducts()
    idproduct= int(input("Enter id of the product: "))
    quantity = int(input("Enter the quantity: "))
    price = 0
    controller.addLineProduct(idorder,idproduct,quantity,price)


def removeLineProduct(order):
    linesProducstOrder(order)
    idline =int(input("Enter the id of the line product: "))
    controller.delLineProduct(idline)
    


def updateOrder(idorder,option):
    order = controller.getOrder(idorder)
    if(option == 1):
        table = int(input("Enter a new table: "))
        order.setTable(table)
        controller.updateOrder(idorder,order)
    elif(option == 2):
        client = input("Enter a new client: ")
        order.setClient(client)
        controller.updateOrder(idorder,order)
    elif(option == 3):
        pax = int(input("Enter a new pax: "))
        order.setPax(pax)
        controller.updateOrder(idorder,order)
    elif(option == 4):
        waiter = input("Enter a new waiter: ")
        order.setWaiter(waiter)
        controller.updateOrder(idorder,order)
    elif(option == 5):
        addLineProduct(idorder)
    elif(option == 6):
        removeLineProduct(order)
    elif(option == 8):
        linesProducstOrder(order)

def updateLineProduct(idline,option):
    lineproduct = controller.getLineProdut(idline)
    if(option == 1):
        product_id = int(input("Enter a new product id: "))
        lineproduct.setProductID(product_id)
        controller.updateLineProduct(idline,lineproduct)
    elif(option == 2):
        quantity = int(input("Enter a new quantity: "))
        lineproduct.setQuantity(quantity)
        controller.updateLineProduct(idline,lineproduct)
def deleteOrder():
    idorder = int(input("Enter id of the Order: "))
    controller.delOrder(idorder)

def getOrders():
    orders  = controller.getOrders()
    for i in range(len(orders)):
        for id, order in orders[i].items():
            print("Id:",id)
            print("\tTable:",order.getTable())
            print("\tClient:",order.getClient())
            print("\tPax:",order.getPax())
            print("\tWaiter:",order.getWaiter())
            print("\tPriceTotal:",order.getPriceTotal())
            print("\tLineProducts:",order.getLineProducts())
            print("\tState:",order.getState())

def getorder():
    idorder = int(input("Enter id of the Order: "))
    order =controller.getOrder(idorder)
    print("Id:",idorder)
    print("\tTable:",order.getTable())
    print("\tClient:",order.getClient())
    print("\tPax:",order.getPax())
    print("\tWaiter:",order.getWaiter())
    print("\tPriceTotal:",order.getPriceTotal())
    print("\tLineProducts:",order.getLineProducts())
    print("\tState:",order.getState())

def confirmOrder():
    idorder = int(input("Enter id of the Order: "))
    controller.confirmOrder(idorder)

while True:
    print("1.- Create Order")
    print("2.- Update Order")
    print("3.- Delete Order")
    print("4.- Get All Order")
    print("5.- Get a Order")
    print("6.- Confirm state of the Order")
    print("7.- Exit")
    option = int(input("Enter the option: "))
    if(option == 7):
        print("Good bye!")
        break
    elif(option == 1):
        createOrder()
    elif(option == 2):
        idorder = int(input("Entre id of the Order: "))
        while True:
            print("1.- Update table")
            print("2.- Update client")
            print("3.- Update pax")
            print("4.- Update waiter")
            print("5.- Add a lineProduct")
            print("6.- Remove a lineProduct")
            print("7.- update a lineProduct")
            print("8.- List line product")
            print("9.- Exit")
            option = int(input("Enter the option: "))
            if(option == 9):
                print("Good bye!")
                break
            elif(option == 1):
                updateOrder(idorder,option)
            elif(option == 2):
                updateOrder(idorder,option)
            elif(option == 3):
                updateOrder(idorder,option)
            elif(option == 4):
                updateOrder(idorder,option)
            elif(option == 5):
                updateOrder(idorder,option)
            elif(option == 6):
                updateOrder(idorder,option)
            elif(option == 7):
                idline =int(input("Enter the id of the line product: "))
                while True:
                    print("1.- Update product id")
                    print("2.- Update quantity")
                    print("3.- Exit")
                    option = int(input("Enter the option: "))
                    if(option == 3):
                        print("Good bye!")
                        break
                    elif(option == 1):
                        updateLineProduct(idline,option)
                    elif(option == 2):
                        updateLineProduct(idline,option)
                    else:
                        print("Option no exist!")
            elif(option == 8):
                updateOrder(idorder,option)
            else:
                print("Option no exist!")
    elif(option == 3):
        deleteOrder()
    elif(option == 4):
        getOrders()
    elif(option == 5):
        getorder()
    elif(option == 6):
        confirmOrder()
    else:
        print("Option no exist!")