class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)

        t1 = l1
        t2 = l2

        current = dummy
        carry = 0

        while t1 or t2:

            sum1 = carry

            if t1:
                sum1 += t1.val

            if t2:
                sum1 += t2.val
            
            newNode = ListNode(sum1 % 10)
            carry = sum1//10

            current.next = newNode
            current = current.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

            if carry:
                newNode = ListNode(carry)
                current.next = newNode

        return dummy.next
