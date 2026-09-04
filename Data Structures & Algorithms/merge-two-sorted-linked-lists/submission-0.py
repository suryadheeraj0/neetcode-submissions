# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(0)
        curr_node = new_list
        curr_a = list1
        curr_b = list2
        while curr_a and curr_b:
            if curr_a.val<curr_b.val:
                curr_node.next = curr_a
                curr_a = curr_a.next
            else:
                curr_node.next = curr_b
                curr_b = curr_b.next
            curr_node = curr_node.next
        while curr_a:
            curr_node.next = curr_a
            curr_a = curr_a.next
            curr_node = curr_node.next
        while curr_b:
            curr_node.next = curr_b
            curr_b = curr_b.next
            curr_node = curr_node.next
        return new_list.next
        