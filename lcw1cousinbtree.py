"""Submitted by thr3sh0ld"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dictl = {}
        level = 0
        parent = None
        def travel(root, parent, level): #recursion funtion for left and right leaf checking and storing
            if root is None:
                return None
            old_level = level
            dictl[root.val] = (parent, level) 
            parent = root.val
            if root.left:
                level += 1
                travel(root.left, parent, level)
            level = old_level
            if root.right:
                level += 1
                travel(root.right, parent, level)             
        travel(root, parent, 0)
        #checking whether cousin or not
        if x in dictl and y in dictl:
            if dictl[x][0] == dictl[y][0]:
                return False
            elif dictl[x][1] != dictl[y][1]:
                return False
            return True
        return False
