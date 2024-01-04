class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        print(mp)
        count = 0
        for v in mp:
            if mp[v] == 1:
                return -1
            else:
                if mp[v]%3 == 0:
                    count += mp[v]//3 
                else:
                    count += mp[v]//3 + 1
        return count
            
            