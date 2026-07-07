class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA is not pointerB:

            if pointerA:
                pointerA = pointerA.next 
            else:
                pointerA = headB

            if pointerB:
                pointerB = pointerB.next
            else: 
                pointerB = headA

        return pointerA
