class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mp = {mx:0}
        n = len(nums)
        ans = 0
        i = 0
        j = 0
        while j<n:
            if nums[j] not in mp:
                mp[nums[j]] = 1
            else:
                mp[nums[j]] += 1
            if mp[mx]>=k:
                while mp[mx]>=k and i<=j:
                    ans+=n-j
                    mp[nums[i]] -=1
                    i+=1
            j+=1
        return ans