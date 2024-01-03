class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        mp = []
        ans  = 0
        for i in bank:
            c = i.count('1')
            if c!=0:
                mp.append(c)
        if len(mp)<2:
            return 0
        for i in range(len(mp)-1):
            ans += mp[i]*mp[i+1]
        return ans
        
        
