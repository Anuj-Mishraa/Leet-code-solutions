class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mj = len(nums)//2
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] += 1
                if mp[i]>mj:
                    return i
            else:
                mp[i] = 1
        for i in mp:
            if mp[i]>mj:
                return i

        
                