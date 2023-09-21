class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1+nums2)
        n =  len(merged)
        if n%2==0:
            median = (merged[n//2]+merged[(n//2)-1])/2
        else:
            median = merged[n//2]
        return median