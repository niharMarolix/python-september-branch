class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def preorder(self, root):
        if not root:
            return None
        
        else:
            stack = [root]

        while stack:
            currentNode = stack.pop()


            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)

            currentNode.left = None
            if stack:
                currentNode.right = stack[-1]
            else:
                currentNode.right = None
    


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(8)

sol = Solution()

sol.preorder(root)


currentNode = root
while currentNode:
    print(currentNode.val, end="->")
    currentNode= currentNode.right
print("None")