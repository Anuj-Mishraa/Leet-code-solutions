class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1, n2 in zip(nums1,nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse = True)
        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum+=n1
            heapq.heappush(minHeap,n1)

            if len(minHeap)>k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            if len(minHeap)==k:
                res = max(res,n1Sum*n2)
        return res
    # def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    #     score = 0
    #     n = len(nums1)
    #     data = [0] * k
    #     result = []
    #     self.combinationUtil(nums1,data, 0, n - 1, 0, k, result)
    #     prod = [] 
    #     for i in result:
    #         prod.append(np.prod(i))
    #     data = [0] * k
    #     result = []
    #     self.combinationUtil(nums2,data, 0, n - 1, 0, k, result)
    #     for i in range(len(result)):
    #         score = max(score,(prod[i]*min(result[i]))) 
    #     return score
        


    # def combinationUtil(self,arr, data, start, end, index, r, ans):
    #     if index == r:
    #         temp = []
    #         for j in range(r):
    #             temp.append(data[j])
    #         ans.append(temp) 
    #         return
    #     i = start
    #     while i <= end and end - i + 1 >= r - index:
    #         data[index] = arr[i]
    #         self.combinationUtil(arr, data, i + 1, end, index + 1, r, ans)
    #         i += 1