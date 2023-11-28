class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None

def l_c_a(root, n1,n2):
    if root is None:
        return None
    
    if root.val == n1.val or root.val == n2.val:
        return root
    
    leftLca = l_c_a(root.left, n1, n2)
    rightLca = l_c_a(root.right, n1, n2)

    if leftLca is not None and rightLca is not None:
        return root
    
    return leftLca if leftLca is not None else rightLca

root = z = TreeNode(1)
root.left =a =  TreeNode(3)
root.right =b =  TreeNode(2)
root.left.right =d =  TreeNode(7)
root.right.right = e = TreeNode(8)
root.right.left = y = TreeNode(9)

nodeOne = y
nodeTwo = e

print((l_c_a(root, nodeOne, nodeTwo)).val)