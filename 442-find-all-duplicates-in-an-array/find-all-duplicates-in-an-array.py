class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        for i in mp:
            if mp[i]>1:
                ans.append(i)
        return ans
        
            
