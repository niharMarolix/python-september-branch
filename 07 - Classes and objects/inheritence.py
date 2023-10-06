class Utensils: # PARENT
    def store(self):
        return("I am used for storing food items or liquid items")

class Patila(Utensils): # CHILD
    def storing(self):
        print("I am used for storing milk")

raj = Patila()
print(raj.store())