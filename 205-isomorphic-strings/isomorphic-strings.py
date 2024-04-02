class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        c = 1
        for i in s:
            if i not in mp1:
                mp1[i] = c
                c+=1
        c= 1
        for i in t:
            if i not in mp2:
                mp2[i] = c
                c+=1
        for i in range(len(s)):
            if mp1[s[i]]!=mp2[t[i]]:
                return False
        return True
        
