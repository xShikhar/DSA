# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inMap = {}
        
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        
        def helper(preStart, preEnd, inStart, inEnd ):

            if preStart > preEnd or inStart > inEnd:
                return None
            
            root = TreeNode(preorder[preStart])

            inRoot = inMap[root.val]

            numsLeft = inRoot - inStart

            root.left = helper(1 + preStart, preStart + numsLeft, inStart , inRoot - 1)
            root.right = helper(1 + preStart + numsLeft, preEnd, inRoot + 1 , inEnd)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
