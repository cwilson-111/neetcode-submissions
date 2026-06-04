# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        current = res
        carry = 0         
        
        while l1 or l2 or carry:
            # get the values, defaulting to 0 if a list has already ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # calculate the total sum for this column
            column_sum = val1 + val2 + carry
            
            # update the carry and calculate the single digit to store
            carry = column_sum // 10       # 18 // 10 = 1
            digit_to_store = column_sum % 10  # 18 % 10 = 8
            
            # create a NEW ListNode object and link it
            current.next = ListNode(digit_to_store)
            
            # move all pointers forward safely
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return res.next

            
            