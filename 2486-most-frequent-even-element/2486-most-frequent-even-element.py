class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = {}
        for i in set(nums):
            if i%2==0:
                if nums.count(i) not in res:
                    res[nums.count(i)] = i
                else:
                    res[nums.count(i)] = min(res[nums.count(i)],i)
        if res=={}:
            return -1
        return res[max(res.keys())]
        