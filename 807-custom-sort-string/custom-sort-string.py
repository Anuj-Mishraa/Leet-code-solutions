class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        ans = ''
        for i in s:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        for i in order:
            if i in mp:
                ans += i*mp[i]
                mp[i]=0
        for i in s:
            if i not in order:
                ans+=i
        return ans