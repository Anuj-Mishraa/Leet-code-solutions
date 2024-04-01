class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sm = 0
        n = len(nums)
        ans = n+1

        for j in range(n):
            sm+=nums[j]
            while(sm>=target):
                ans = min(ans,j-i+1)
                sm-=nums[i]
                i+=1
        return 0 if ans==n+1 else ans