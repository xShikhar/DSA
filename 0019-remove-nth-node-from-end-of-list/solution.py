class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast hits the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow is now right before the node to remove
        slow.next = slow.next.next

        return dummy.next
