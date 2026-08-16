from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        q = deque([(root, 0)])  # (node, id)

        while q:
            size = len(q)
            _, mmin = q[0]     # id of first node in this level, used to rebase
            first = last = 0

            for i in range(size):
                node, cur_id = q.popleft()
                cur_id -= mmin  # rebase to avoid overflow

                if i == 0:
                    first = cur_id
                if i == size - 1:
                    last = cur_id

                if node.left:
                    q.append((node.left, cur_id * 2 + 1))
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))

            ans = max(ans, last - first + 1)

        return ans
