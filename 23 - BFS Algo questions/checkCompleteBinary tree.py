class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = self.right = None

def checkCompleteBinaryTree(root):
    if not root:
        return -1
    
    queue = [root]
    leaf_started = False

    while queue:
        node = queue.pop(0)

        if node:
            if leaf_started:
                return False
            
            queue.append(node.left)
            queue.append(node.right)

            if not node.left or node.right:
                leaf_started = True

        else:
            for i in queue:
                if i:
                    return False 
    
    return True
            


root = TreeNode(231)
root.right = TreeNode(312)
root.right.right  = TreeNode(324)
root.right.left  = TreeNode(324)
root.left = TreeNode(4324)
root.left.right = TreeNode(231423)
root.left.left = TreeNode(231423)
root.right


'''
                  231
                             312
        4324            324              324                  
 231423          231423
'''


res = checkCompleteBinaryTree(root)
if  res == True:
    print("YIIACBT")

elif res == -1:
    print("no root provided")
else:
    print("NIINACBT")