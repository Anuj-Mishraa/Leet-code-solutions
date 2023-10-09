class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        # if nums.count(target)==1:
        #     a = nums.index(target)
        #     return [a,a]
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==target:
        #         ans.append(i)
        #         break
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         ans.append(i)
        #         break
        i = bisect.bisect_left(nums,target,0,len(nums))
        j = bisect.bisect_right(nums,target,0,len(nums))-1
        return [i,j]
            
