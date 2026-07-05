class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next

        return True
