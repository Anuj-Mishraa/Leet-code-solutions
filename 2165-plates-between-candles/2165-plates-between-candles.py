class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plt_idx = [i for i in range(len(s)) if s[i]=='|']
        ans = []
        for it in queries:
            l = it[0]
            r = it[1]
            i = bisect.bisect_left(plt_idx,l,0,len(plt_idx))
            j = bisect.bisect_right(plt_idx,r,0,len(plt_idx))-1
            if j<=i:
                ans.append(0)
            else:
                ans.append(plt_idx[j]-plt_idx[i]-(j-i))
        return ans