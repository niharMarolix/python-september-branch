class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = self.right = None

def level_sum(root, target):
    if not root:
        return -1
    
    queue = [(root,0)]
    currentLevel = 0
    sumAtTargetLevel = 0


    while queue:
        node, level = queue.pop(0)

        if level == target:
            sumAtTargetLevel = sumAtTargetLevel+node.value

        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right,level+1))
    
    return sumAtTargetLevel



root = TreeNode(231)
root.right = TreeNode(312)
root.right.right  = TreeNode(324)
root.left = TreeNode(4324)
root.left.right = TreeNode(231423)


targetLevel = 2
result = level_sum(root, targetLevel)
print(result)