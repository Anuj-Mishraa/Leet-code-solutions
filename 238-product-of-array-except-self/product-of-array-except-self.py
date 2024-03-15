class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        c_zero = 0
        ans = []
        for i in nums:
            if i!=0:
                product*=i
            else:
                c_zero += 1
        for i in nums:
            if i!=0 and c_zero==0:
                ans.append(product//i)
            elif(i==0 and c_zero==1):
                ans.append(product)
            else:
                ans.append(0)
        return ans
        
