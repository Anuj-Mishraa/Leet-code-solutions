# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        while slow is not None:
            next_n = slow.next
            slow.next = pre
            pre = slow
            slow = next_n
        left, right = head,pre
        while right:
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        return True