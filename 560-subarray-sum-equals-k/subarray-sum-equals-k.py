from collections import defaultdict 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        mp = defaultdict(int)
        mp[0] = 1
        pre = 0
        cnt = 0
        for i in range(n):
            pre += nums[i]
            remove = pre-k
            cnt += mp[remove]
            mp[pre] += 1 
        return cnt
            