class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i,val in enumerate(nums):
            if i<=curr:
                curr = max(curr,i+val)
        return curr>=len(nums)-1