# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nodes = []

        def dfs(node,row,col):
            if not node:
                return
            
            nodes.append((col,row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)

        dfs(root,0,0)

        nodes.sort(key=lambda x: (x[0],x[1],x[2]))

        result = defaultdict(list)

        for col,row,val in nodes:
            result[col].append(val)

        return [result[col] for col in sorted(result.keys())]
