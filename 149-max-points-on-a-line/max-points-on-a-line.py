
from math import gcd
class Solution:
    def __init__(self):
        self.stor = defaultdict(set)
    def slop_check(self,A,B):
        x1,y1 = A[0],A[1]
        x2,y2 = B[0],B[1]
        try:
            slop = (y2-y1)/(x2-x1)
            c = y1-slop*x1
        except:
            slop = float('inf')
            c = x1
        self.stor[(slop,c)].add((x1,y1))
        self.stor[(slop,c)].add((x2,y2))
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        n = len(points)
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                self.slop_check(points[i],points[j])
        print(self.stor)
        for i in self.stor:
            ans = max(ans,len(self.stor[i]))
        return ans

        