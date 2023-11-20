
'''
pre - root->left->right
in - left->root->right
post - left->right->root

'''


class newNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.key, end =" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end =" ")
        inorder(root.right)


# def postorder(root):




root = newNode(1)
root.left = newNode(3)
root.right = newNode(2)
root.left.right = newNode(7)
root.right.right = newNode(8)

# preorder(root)
inorder(root)