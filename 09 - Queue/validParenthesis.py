class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)  ==0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("queue id empty")
            return -1



def isValidParenthesis(s):
    q = Queue()

    for i in s:
        if i in '([{':
            q.enqueue(i)
        elif i in ')]}':
            if q.isEmpty():
                return False
            top= q.dequeue()
            if (i==")" and top !="(") or (i=="}" and top !="{") or (i=="]" and top !="["):
                return False
    return q.isEmpty()

print(isValidParenthesis("(([]))"))
print(isValidParenthesis( "({[})"))