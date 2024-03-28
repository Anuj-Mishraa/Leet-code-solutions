class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mp = {}
        n = len(nums)
        ans = 0
        i = 0
        j = 0
        while j<n:
            if nums[j] not in mp:
                mp[nums[j]] = 1
            else:
                mp[nums[j]] += 1
            if mp[nums[j]]>k:
                while mp[nums[j]]>k and i<j:
                    mp[nums[i]]-=1
                    i+=1
            if mp[nums[j]]<=k:
                ans=max(ans,j-i+1)
            j+=1
        return ans
            
                