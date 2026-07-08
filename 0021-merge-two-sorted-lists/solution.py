class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr3 = dummy
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next

        # attach whichever list has leftovers
        curr3.next = curr1 if curr1 else curr2

        return dummy.next
