class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxi = float('-inf')

        def maxpath(node):
            if node is None:
                return 0

            maxL = max(0, maxpath(node.left))
            maxR = max(0, maxpath(node.right))

            self.maxi = max(self.maxi, node.val + maxL + maxR)

            return max(maxL, maxR) + node.val

        maxpath(root)

        return self.maxi
