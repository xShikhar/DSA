class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        l_to_r = True
        q = deque([root])

        while q:
            size = len(q)
            level = deque()

            for _ in range(size):
                
                node = q.popleft()

                if l_to_r:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(list(level))
            l_to_r = not l_to_r
        
        return result
