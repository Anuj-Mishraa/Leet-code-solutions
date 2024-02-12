class Solution(object):
    def majorityElement(self, nums):
        maj = nums[0]
        count = 1
        n = len(nums)
        for i in range(1,n):
            if(count==0):
                count+=1
                maj = nums[i]
            elif(nums[i]==maj):
                count+=1
            else:
                count-=1
        return maj