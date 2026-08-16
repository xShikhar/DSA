# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0 

        def height(node):
            
            if node == None:
                return 0
            
            lh = height(node.left)
            rh = height(node.right)

            self.best =  max(self.best,lh+rh)
            return max(lh,rh) + 1

        height(root)
        return self.best
