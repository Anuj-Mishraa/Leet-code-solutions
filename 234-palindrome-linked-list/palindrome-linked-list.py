# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        temp = head
        while temp:
            st.append(temp.val)
            temp = temp.next
        while st:
            a = st.pop()
            if a != head.val:
                return False
            head = head.next
        return True