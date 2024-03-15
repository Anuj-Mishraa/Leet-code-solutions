class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            a = nums[i]
            target = -a
            s=i+1
            e=n-1
            while s<e:
                if(nums[s]+nums[e]==target):
                    ans.add((nums[i],nums[s],nums[e]))
                    while (s<e and nums[s]==nums[s+1]):
                        s+=1
                    while (s<e and nums[e]==nums[e-1]):
                        e-=1
                    s+=1
                    e-=1
                elif(nums[s]+nums[e]>target):
                    e-=1
                else:
                    s+=1
            while(i+1<n and nums[i+1]==nums[i]):
                i+=1
        return ans
                
