class Solution:
    def removeStars(self, s: str) -> str:

        count, ans, s = 0, deque(),s[::-1] 

        for ch in s:
            if ch == '*': count+=1
            elif count  : count-=1
            else        : ans.appendleft(ch) 

        return  ''.join(ans)