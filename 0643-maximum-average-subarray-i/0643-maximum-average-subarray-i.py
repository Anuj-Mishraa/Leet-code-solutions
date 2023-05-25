class Solution:

 
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        s = sum(nums[0 : k])
        mx = s

        # [1,12,-5,-6,50,3],   k = 4

        

        for i in range(0, len(nums) - k):
            s = s + nums[i + k] - nums[i]
            mx = max(mx, s)

        return mx / k

        # 1,12,-5,-6,50,3
        # [1 ,13, 8, 2, 52, 55]
