# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        idx = length - n
        i = 0
        prev, curr = None, head

        while curr:
            if i == idx:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                return head
            prev = curr
            i += 1
            curr = curr.next

        return None
        
        

        