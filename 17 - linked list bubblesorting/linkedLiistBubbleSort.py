class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def bubbleSort(self):
        if self.head is None:
            print("add elements to sort elements")
        else:
            end = None
            while end != self.head:
                prev = None
                current = self.head
                while current.next != end:
                    nextNode = current.next
                    if current.data>nextNode.data:
                        current.next = nextNode.next
                        nextNode.next = current

                        if prev:
                            prev.next = nextNode
                        else:
                            self.head = nextNode
                        current, nextNode = nextNode, current
                    prev = current
                    current = nextNode
                end = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
    
linkedList = LinkedList()
linkedList.add(5)
linkedList.add(2)
linkedList.add(3)
linkedList.add(1)
linkedList.add(8)
linkedList.add(7)
linkedList.add(9)
linkedList.add(6)
linkedList.add(4)
print("before sorting")
linkedList.display()
print("--------------------------------------------")
print("after sorting")
linkedList.bubbleSort()
linkedList.display()


