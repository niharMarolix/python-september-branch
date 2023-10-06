class Car: # parnt
    def __init__(self, model, colour, price):
        self.model = model
        self._colour = colour # protected variable
        self.__price = price # private variable
        
    def colour(self):
         return(f"color is {self._colour}")

    def price(self):
        return(f'price is {self.__price}')

    def model(self):
        return(f'model is {self.model}')
    
class CarOne(Car): # child
    def colour(self):
        return(f"color is {self._colour}")
    
    def price(self):
        # self.__price = 10
        return(f'price is {self.__price}')

Tata  = CarOne("nexon","red",1000000)
print(Tata.price())