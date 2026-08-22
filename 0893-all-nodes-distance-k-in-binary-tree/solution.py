class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent = {}

        def parentnode(node,par):
            
            if not node:
                return 
            
            parent[node] = par
            parentnode(node.left,node)
            parentnode(node.right,node)
        
        parentnode(root,None)

        visited = set()
        visited.add(target)
        queue = [target]
        dis = 0

        while queue:

            if dis == k:
                return [node.val for node in queue]

            next_queue = []

            for node in queue:
                for neighbour in (node.left,node.right,parent[node]):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        next_queue.append(neighbour)
                    
            queue = next_queue
            dis += 1
        
        return []
