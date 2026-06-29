# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the head of the output list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop as long as there are nodes to process or a carry remaining
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for this position
            total = val1 + val2 + carry
            
            # Update carry and calculate the digit to store
            carry = total // 10
            digit = total % 10
            
            # Append the new digit node to the result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next