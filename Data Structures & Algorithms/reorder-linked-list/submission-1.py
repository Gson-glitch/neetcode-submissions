# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list
        # fast = head.next rather than head for us to split the list equally
        # for a list with even length.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second = slow.next
        prev, slow.next = None, None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two halves
        first, second = head, prev
        # We use while second: instead of while first: because the second half is 
        # always equal to or shorter than the first half.
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        