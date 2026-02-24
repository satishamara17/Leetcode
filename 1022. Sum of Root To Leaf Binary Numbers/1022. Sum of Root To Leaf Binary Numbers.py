#
# Problem: 1022. Sum of Root To Leaf Binary Numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/1930155907/?envType=daily-question&envId=2026-02-24
# Language: python3
# Date: 2026-02-24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            

            current = (current << 1) | node.val
            
            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)        
