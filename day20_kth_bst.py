# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3sh0ld using Inorder traversal
#learnt exception rasing for handling normal cases
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def INOD(root,k):
            if root:
                k = INOD(root.left,k)
                if k == 1:
                    raise error(root.val)
                k = INOD(root.right,k-1)
            return k
        try:
            INOD(root,k)
        except error as res: 
            return res
        
        