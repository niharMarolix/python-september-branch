from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = self.left = None

def binaryTree():
    root = TreeNode("Mancherial")
    root.left = TreeNode("YGG")
    root.left.left = TreeNode("Warangal")
    root.left.right = TreeNode("Secunderabad")
    root.right = TreeNode("Medak")
    root.right.right = TreeNode("Kurnool")

    return root

def bfsLot(tree):
    if not tree:
        return []

    visitedQueue = set()
    explored = []
    queue = deque([tree])

    while queue:
        currentNode = queue.popleft()

        if currentNode not in visitedQueue:
            visitedQueue.add(currentNode)
            explored.append(currentNode.value)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return explored




root = binaryTree()


result = bfsLot(root)
print(result)