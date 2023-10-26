class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkeList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data) # data  = Shruti
        if not self.head:   # invalid
            self.head = newNode
        else:
            current = self.head         # current = rashmika
            while current.next:          # invalid
                current = current.next # current - rashmika
            current.next = newNode   # rashmika.next = Shruti

    def display(self):
        current = self.head # current = nikhil
        while current: # invalid
            print(current.data, end = "--->") # nikhil--->Rashmika--->Shruti--->None
            current = current.next
        print("None")

linkedList = SinglyLinkeList()
linkedList.append("Nikhil")
linkedList.append("Rashmika")
linkedList.append("Shruti")
linkedList.display()