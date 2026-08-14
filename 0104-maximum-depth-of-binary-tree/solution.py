# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):

            if node == None:
                return 0

            lh = maxDepth(node.left)
            rh = maxDepth(node.right)

            return 1 + max(lh,rh)
            
        return maxDepth(root)

