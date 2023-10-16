class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            nums = [(nums[j]+nums[j+1])%10 for j in range(len(nums)-1)]
        return nums[0]
            