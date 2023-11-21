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

arr = [3,21,534,6,745,7567,7,5,75,757]
sortedArray = sorted(arr)
print(sortedArray)

res = sortedArrayToTree(sortedArray)

print()