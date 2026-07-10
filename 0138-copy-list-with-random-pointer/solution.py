class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # pass 1: create all clones, map original -> clone
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # pass 2: wire next and random using the map
        current = head
        while current:
            clone = old_to_new[current]
            clone.next = old_to_new.get(current.next)
            clone.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]
