class TreeNode:
   
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    

A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(6)
D = TreeNode(1)
E = TreeNode(3)
F = TreeNode(5)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

def search_bst(node,target):

    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val:
        return search_bst(node.left, target)
    
    else:
        return search_bst(node.right,target)


