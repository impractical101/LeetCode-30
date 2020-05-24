# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3sh0ld using recursion and recursively checking for root node
class Solution:
    def check(self, root, x):
        if not root:
            return TreeNode(x)
        if x < root.val:
            root.left = self.check(root.left, x)
        else:
            root.right = self.check(root.right, x)
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = None
        for i in range(len(preorder)):
            node = preorder[i]
            root = self.check(root, node)
        return root
        
    
        
        
        
        
        
        
        