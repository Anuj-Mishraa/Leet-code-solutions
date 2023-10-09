class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        if nums.count(target)==1:
            a = nums.index(target)
            return [a,a]
        ans = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                ans.append(i)
                break
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
                break
        return ans[::-1]
            
