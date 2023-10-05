class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in set(nums):
            if nums.count(i)<=n/3:
                for j in range(nums.count(i)):
                    nums.remove(i)
        return list(set(nums))