# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        curr = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            curr = curr.next
        slow = slow.next
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        curr.next = None
        first_node = head
        second_node = prev
        flag = True
        while first_node and second_node:
            first_next = first_node.next
            second_next = second_node.next
            
            first_node.next = second_node
            second_node.next = first_next
            
            first_node = first_next
            second_node = second_next