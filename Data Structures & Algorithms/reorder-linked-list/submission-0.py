class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # STEP 1: Find middle
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # STEP 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # STEP 3: Merge
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2