class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp1 = set()
        mp2 = set()
        ans = 0
        for num in arr1:
            s = str(num)
            l = len(s)

            for j in range(1,l+1):
                mp1.add(s[:j])
        
        for num in arr2:
            s = str(num)
            l = len(s)

            for j in range(1,l+1):
                mp2.add(s[:j])
        # print(mp1,mp2)
        for i in mp1:
            if i in mp2:
                ans = max(ans,len(i))
        return ans

