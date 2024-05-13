# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: # type: ignore

        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode(0)

        # Used this to build the new list starting at the dummy node
        curr = dummy
        
        # Loop until the end of either l1 or l2 is reached
        while l1 and l2:

            # Compare current nodes of both lists
            if l1.val < l2.val:

                # If l1's value is smaller, append it to the merged list
                curr.next = l1
                
                # Move to the next node in l1
                l1 = l1.next
            else:
                
                # If l2's value is smaller or equal, append it to the merged list
                curr.next = l2
                
                # Move to the next node in l2
                l2 = l2.next
            
            curr = curr.next
        
        # At this point, at least one of l1 or l2 is null. Attach the remaining part of the non-null list to the merged list
        curr.next = l1 or l2
        
        # Return the merged list
        return dummy.next
