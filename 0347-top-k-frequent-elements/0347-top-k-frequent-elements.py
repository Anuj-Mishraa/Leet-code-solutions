class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = []
        for i in set(nums):
           mp.append([i,nums.count(i)])
        mp.sort(key=lambda x:x[1],reverse=True)
        ans = []
        for i in range(k):
            ans.append(mp[i][0])
        return ans
