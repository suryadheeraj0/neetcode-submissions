# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node_l1 = l1
        curr_node_l2 = l2
        carry = 0
        res_list = ListNode(0)
        res_node = res_list
        while curr_node_l1 and curr_node_l2:
            su = curr_node_l1.val + curr_node_l2.val + carry
            if su>9:
                res_node.next = ListNode(su%10)
                carry = 1
            else:
                res_node.next = ListNode(su)
                carry = 0
            res_node = res_node.next
            curr_node_l1 = curr_node_l1.next
            curr_node_l2 = curr_node_l2.next
        while curr_node_l1:
            su = curr_node_l1.val + carry
            if su>9:
                res_node.next = ListNode(su%10)
                carry = 1
            else:
                res_node.next = ListNode(su)
                carry = 0
            res_node = res_node.next
            curr_node_l1 = curr_node_l1.next
        while curr_node_l2:
            su = curr_node_l2.val + carry
            if su>9:
                res_node.next = ListNode(su%10)
                carry = 1
            else:
                res_node.next = ListNode(su)
                carry = 0
            res_node = res_node.next
            curr_node_l2 = curr_node_l2.next
        if carry:
            res_node.next = ListNode(carry)
        return res_list.next

