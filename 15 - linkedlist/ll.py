class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # vamshi.next==>None

class LinkedList:
    def __init__(self):
        self.head = None

    def addDataAtEnd(self,data):
        newNodeToBePopulated = Node(data)
        if self.head == None:
            self.head = newNodeToBePopulated
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next =  newNodeToBePopulated

    def prepend(self,data):
        newNodeToBePopulated = Node(data)
        newNodeToBePopulated.next = self.head
        self.head = newNodeToBePopulated

    def delete(self,data):
        if self.head == None:
            print("add some elements to delete element")

        if data == self.head.data:
            self.head = self.head.next
            return
        
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = "-->")
            current = current.next
        print("None")




myList = LinkedList()
myList.addDataAtEnd("Gopi")
myList.addDataAtEnd("Vamshi")
myList.addDataAtEnd("shekhar")
myList.delete("shekhar")
myList.prepend("sandhya")
myList.display()
