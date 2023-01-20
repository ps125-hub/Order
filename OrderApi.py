import requests,json
from Category import Category
from Prodcut import Product
from Ingredient import Ingredient
from Order import Order
from LineProduct import LineProduct
def getIngredientsALL():
    url = "http://localhost:8069/restaurant_app/getIngredient"
    response = requests.request("GET", url)
    if response.ok:
        dataingredients =dict(json.loads(response.text))
        ingredients=[]
        for i  in range(len(dataingredients["data"])):
            idingredient= dataingredients["data"][i]["id"]
            name = dataingredients["data"][i]["name"]
            allergen = dataingredients["data"][i]["allergen"]
            cometari =dataingredients["data"][i]["comentari"]
            products = dataingredients["data"][i]["products"]
            ingredient = Ingredient(name,allergen,cometari,products)
            ingredients.append({idingredient:ingredient})
        return ingredients
    else:
        print("Error")

def getProductsALL():
    url = "http://localhost:8069/restaurant_app/getProduct"
    response = requests.request("GET", url)
    if response.ok:
        dataproducts =dict(json.loads(response.text))
        products=[]
        for i  in range(len(dataproducts["data"])):
            idproduct= dataproducts["data"][i]["id"]
            name = dataproducts["data"][i]["name"]
            description = dataproducts["data"][i]["description"]
            price =dataproducts["data"][i]["price"]
            categories = dataproducts["data"][i]["categories"]
            ingredients = dataproducts["data"][i]["ingredients"]
            product = Product(name,description,price,categories,ingredients)
            products.append({idproduct:product})
        return products
    else:
        print("Error")

def getCategoriesAll():
    url = "http://localhost:8069/restaurant_app/getCategory"
    response = requests.request("GET", url)
    if response.ok:
        datacategories =dict(json.loads(response.text))
        categories=[]
        for i  in range(len(datacategories["data"])):
            idcategory = datacategories["data"][i]["id"]
            name = datacategories["data"][i]["name"]
            description = datacategories["data"][i]["description"]
            parent_id = datacategories["data"][i]["parent_id"]
            products =datacategories["data"][i]["products"]
            category = Category(name,description,parent_id,products)
            categories.append({idcategory:category})
        return categories
    else:
        print("Error")

def getLineProductAll():
    url = "http://localhost:8069/restaurant_app/getLineproduct"
    response = requests.request("GET", url)
    if response.ok:
        datalinesproducts =dict(json.loads(response.text))
        linesproducts=[]
        for i  in range(len(datalinesproducts["data"])):
            idline = datalinesproducts["data"][i]["id"]
            order_id = datalinesproducts["data"][i]["order_id"]
            product_id = datalinesproducts["data"][i]["product_id"]
            quantity =datalinesproducts["data"][i]["quantity"]
            price =datalinesproducts["data"][i]["price"]
            lineproduct = LineProduct(order_id,product_id,quantity,price)
            linesproducts.append({idline:lineproduct})
        return linesproducts
    else:
        print("Error")

def getOrderAll():
    url = "http://localhost:8069/restaurant_app/getOrder"
    response = requests.request("GET", url)
    if response.ok:
        dataordes =dict(json.loads(response.text))
        orders=[]
        for i  in range(len(dataordes["data"])):
            idorder = dataordes["data"][i]["id"]
            table = dataordes["data"][i]["table"]
            client = dataordes["data"][i]["client"]
            pax = dataordes["data"][i]["pax"]
            waiter = dataordes["data"][i]["waiter"]
            priceTotal = dataordes["data"][i]["priceTotal"]
            lineProducts =dataordes["data"][i]["lineProducts"]
            state = dataordes["data"][i]["state"]
            order = Order(table,client,pax,waiter,priceTotal,lineProducts,state)
            orders.append({idorder:order})
        return orders
    else:
        print("Error")

def getIngredientID(idingredient):
    url = "http://localhost:8069/restaurant_app/getIngredient/?idingred="+str(idingredient)
    response = requests.request("GET", url)
    if response.ok:
        dataingredients =dict(json.loads(response.text))
        name = dataingredients["data"][0]["name"]
        allergen = dataingredients["data"][0]["allergen"]
        cometari = dataingredients["data"][0]["comentari"]
        products = dataingredients["data"][0]["products"]
        ingredient = Ingredient(name,allergen,cometari,products)
        return ingredient
    else:
        print("Error")

def getProductID(idproduct):
    url = "http://localhost:8069/restaurant_app/getProduct/?idproduct="+str(idproduct)
    response = requests.request("GET", url)
    if response.ok:
        dataproducts =dict(json.loads(response.text))
        name = dataproducts["data"][0]["name"]
        description= dataproducts["data"][0]["description"]
        price= dataproducts["data"][0]["price"]
        categories= dataproducts["data"][0]["categories"]
        ingredients= dataproducts["data"][0]["ingredients"]
        product = Product(name,description,price,categories,ingredients)

        return product
    else:
        print("Error")

def getCategoryID(idcategory):
    url = "http://localhost:8069/restaurant_app/getCategory/?idcategory="+str(idcategory)
    response = requests.request("GET", url)
    if response.ok:
        categorydata =dict(json.loads(response.text))
        name = categorydata["data"][0]["name"]
        descripcion= categorydata["data"][0]["description"]
        parent_id = categorydata["data"][0]["parent_id"]
        products= categorydata["data"][0]["products"]
        category = Category(name,descripcion,parent_id,products)
        return category
    else:
        print("Error")

def getOrderID(idorder):
    url = "http://localhost:8069/restaurant_app/getOrder/?idorder="+str(idorder)
    response = requests.request("GET", url)
    if response.ok:
        dataorder =dict(json.loads(response.text))
        idorder = dataorder["data"][0]["id"]
        table = dataorder["data"][0]["table"]
        client = dataorder["data"][0]["client"]
        pax = dataorder["data"][0]["pax"]
        waiter = dataorder["data"][0]["waiter"]
        priceTotal = dataorder["data"][0]["priceTotal"]
        lineProducts =dataorder["data"][0]["lineProducts"]
        state = dataorder["data"][0]["state"]
        order = Order(table,client,pax,waiter,priceTotal,lineProducts,state)            
        return order
    else:
        print("Error")


def getLineProduct(idline):
    url = "http://localhost:8069/restaurant_app/getLineproduct/?idline="+str(idline)
    response = requests.request("GET", url)
    if response.ok:
        datalineproduct =dict(json.loads(response.text))
        order_id = datalineproduct["data"][0]["order_id"]
        product_id = datalineproduct["data"][0]["product_id"]
        quantity =datalineproduct["data"][0]["quantity"]
        price =datalineproduct["data"][0]["price"]
        lineproduct = LineProduct(order_id,product_id,quantity,price)
        return lineproduct
    else:
        print("Error")

#create
def postOrder(order):
    url = "http://localhost:8069/restaurant_app/addOrder"
    payload = {
	"table":order.getTable(),
    "client":order.getClient(),
    "pax":order.getPax(),
    "waiter":order.getWaiter(),
    "lineProducts":order.getLineProducts(),
    }
    response = requests.request("POST", url,json=payload)
    if response.ok:
        orderdata =dict(json.loads(response.text))
        print(orderdata)
        return orderdata["result"]["data"]
    else:
        print("Error")
def postLineProduct(lineproduct):
    url = "http://localhost:8069/restaurant_app/addLineproduct"
    payload = {
	"order_id":lineproduct.getOrderID(),
    "product_id":lineproduct.getProductID(),
    "quantity":lineproduct.getQuantity()
    }
    response = requests.request("POST", url,json=payload)
    if response.ok:
        lineproductdata =dict(json.loads(response.text))
        print(lineproductdata)
    else:
        print("Error")

#update
def endOrder(idorder):
    url = "http://localhost:8069/restaurant_app/endOrder"
    payload = {
    "id":idorder,
	"state":"C"
    }
    response = requests.request("PUT", url,json=payload)
    if response.ok:
        orderdata =dict(json.loads(response.text))
        print(orderdata)
    else:
        print("Error")
def putOrder(idorder,order):
    url = "http://localhost:8069/restaurant_app/updateOrder"
    payload = {
    "id":idorder,
	"table":order.getTable(),
    "client":order.getClient(),
    "pax":order.getPax(),
    "waiter":order.getWaiter(),
    "priceTotal":order.getPriceTotal(),
    "lineProducts":order.getLineProducts(),
    "state":order.getState()
    }
    response = requests.request("PUT", url,json=payload)
    if response.ok:
        orderdata =dict(json.loads(response.text))
        print(orderdata)
    else:
        print("Error")

def putLineProduct(idline,lineproduct):
    url = "http://localhost:8069/restaurant_app/updateLineperoduct"
    payload={}
    payload["id"] = idline
    product_id = lineproduct.getProductID()
    if str(product_id).isdigit() == True:
        payload["product_id"]= product_id
    else:
        payload["product_id"] = product_id[0]
    quantity = lineproduct.getQuantity()
    payload["quantity"] = quantity
    #payload = {
    #"id":idline,
	#"order_id":lineproduct.getOrderID()[0],
    #"product_id":lineproduct.getProductID()[0],
    #"quantity":lineproduct.getQuantity()
    #}
    response = requests.request("PUT", url,json=payload)
    if response.ok:
        lineproductdata =dict(json.loads(response.text))
        print(lineproductdata)
    else:
        print("Error")
#delete
def deleteOrder(idorder):
    url = "http://localhost:8069/restaurant_app/delOrder"
    payload = {
    "id":idorder
    }
    response = requests.request("DELETE", url,json=payload)
    if response.ok:
        orderdata =dict(json.loads(response.text))
        print(orderdata)
    else:
        print("Error")

def deleteLineProduct(idline):
    url = "http://localhost:8069/restaurant_app/delLineproduct"
    payload = {
    "id":idline
    }
    response = requests.request("DELETE", url,json=payload)
    if response.ok:
        lineproductdata =dict(json.loads(response.text))
        print(lineproductdata)
    else:
        print("Error")