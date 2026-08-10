# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if list is empty: 
        if (head == None):
            return head

        # iterate thru all the nodes 

        prev = None
        curr = head
        
        while (curr != None):
            nxt = curr.next
            # switch two nodes at a time
            curr.next = prev 
            prev = curr 
            curr = nxt
            
        return prev
