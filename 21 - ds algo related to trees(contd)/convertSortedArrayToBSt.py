class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None


def sortedArrayToTree(sortedArray):
    if not sortedArray:
        return None
    
    else:

        mid = len(sortedArray)//2

        root = TreeNode(sortedArray[mid]) # creating a root node

        root.left = sortedArrayToTree(sortedArray[:mid])
        root.right = sortedArrayToTree(sortedArray[mid+1:])

        return root
    
def displayTree(root,level = 0, pre = "r:  "):
    
    if root is not None:
        print(" " *  (level * 4) +pre +str(root.val))
        if root.left is not None or root.right is not None:
            displayTree(root.left,level + 1, "//")
            displayTree(root.right, level + 1, "\\")



arr = [3, 5, 6, 7, 21, 75, 534, 745, 757, 7567]
sortedArray = sorted(arr)
print(sortedArray)

res = sortedArrayToTree(sortedArray)

print(displayTree(res))