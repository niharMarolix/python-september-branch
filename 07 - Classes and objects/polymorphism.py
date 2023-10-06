class Father: # PARENT
    def movement(self):
        return("Father can walk")

class Son(Father): # CHILD
    def movement(self):
        return("5 month old son can crawl")

raj = Son()
print(raj.movement())