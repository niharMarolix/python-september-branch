def addToCart(userIds, name,productName, addTOCart, groceries):
    
    try:
        if name not in userIds:
            raise Exception("User not found, please register with us")
        else:
            if productName not in groceries:
                raise Exception("Product not present in our inventory")
            else:
                addTOCart.append(productName)
                return({
                    "message":f"{productName} is added by user {name}",
                    "data":addTOCart
                })

    except Exception as ex:
        return({
            "message":str(ex),
            "data":None
        })

db = {
    1:"raja",
    2:"Sandhya",
    3:"Vamshi",
    4:"bhargava",
    5:"gopi",
    6:"pusgpavati"
}

addTOCart = []
groceries = ["apples", "bananas", "carrots", "eggs", "milk", "bread", "chicken", "rice", "pasta", "onions"]

userNamesList = list(dict.values(db))
currentCustomerUserName = "raja"
productName = "dvfdsvdfsv"
res = addToCart(userNamesList, currentCustomerUserName, productName, addTOCart, groceries)
print(res)

