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
        
    def size(self):
        return len(self.items)
    

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("queue id empty")
            return -1
        
q = Queue()

q.enqueue("pratyusa")
q.enqueue("kalyan")
q.enqueue("saigopi")
q.dequeue()
q.enqueue("saigopi")
q.enqueue("pratyusa")
q.dequeue()
q.dequeue()
q.dequeue()
