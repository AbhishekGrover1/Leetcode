# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast pointer so that there is gap of n nodes between fast and slow 
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end 
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # slow.next is the node to be deleted; skip it
        slow.next = slow.next.next

        # Return the actual head, which is dummy.next
        return dummy.next