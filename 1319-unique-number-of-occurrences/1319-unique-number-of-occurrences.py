class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = set(arr)
        ans = []
        for i in a:
            ans.append(arr.count(i))
        return len(ans) == len(list(set(ans)))