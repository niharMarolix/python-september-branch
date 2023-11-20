class newNode:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def heightOfTree(node):
    depth = 0
    while node is not None:
        depth = depth+1
        node = node.left

    return depth


root = None
root = newNode(1)
root.left = newNode(3)
root.right = newNode(2)
root.left.right = newNode(7)
root.right.right = newNode(8)


print(heightOfTree(root))
