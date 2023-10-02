class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        longest = cur = 0
        for num in nums:
            if num == mx:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 0
        return longest
        # result = float("-inf")
        # dic = dict()
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)+1):
        #         bit = arr[i:j][0]
        #         for k in arr[i:j]:
        #             bit &= k
        #         if bit not in dic:
        #             dic[bit]=len(arr[i:j])
        #         else:
        #             dic[bit]=max(dic[bit],len(arr[i:j]))
        # for key in dic:
        #     result = max(result,key)
        # return dic[result]
    # def __init__(self):
    #     self.dic = dict()

    # def longestSubarray(self, nums: List[int]) -> int:
    #     result = float("-inf")
    #     self.sab_bit(nums, 0, 0)
    #     for key in self.dic:
    #         result = max(result,key)
    #     return self.dic[result]

    # def sab_bit(self, arr, s, e):
    #     if e == len(arr):
    #         return
    #     elif s > e:
    #         self.sab_bit(arr, 0, e + 1)
    #     else:
    #         bit = arr[s:e+1][0]
    #         for i in arr[s:e + 1]:
    #             bit &= i
    #         if bit not in self.dic:
    #                 self.dic[bit]=len(arr[s:e + 1])
    #         else:
    #             self.dic[bit]=max(self.dic[bit],len(arr[s:e + 1]))
    #         return self.sab_bit(arr, s + 1, e)
        
                