# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count_number_nodes = 0
        curr = head
        while curr:
            count_number_nodes+=1
            curr=curr.next
        node_to_remove = count_number_nodes - n
        if node_to_remove==0:
            head = head.next
            return head
        curr_node = head
        while node_to_remove>1:
            curr_node = curr_node.next
            node_to_remove-=1
        curr_node.next = curr_node.next.next
        return head
        
        