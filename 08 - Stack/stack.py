class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def deleteFromLast(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print("push some data to pop")
        
    def displayStack(self):
        return(self.items)

    def peek(self):
        return(self.items[-1])

    def sizeOfStack(self):
        return(len(self.items))

stack = Stack()
stack.push("black Jeans")
stack.push("brown Khakees")
stack.deleteFromLast()
print(stack.peek())
print(stack.displayStack())