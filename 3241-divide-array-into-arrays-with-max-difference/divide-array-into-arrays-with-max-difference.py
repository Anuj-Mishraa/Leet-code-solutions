class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []

        result = []

        nums.sort()

        for i in range(0, n, 3):
            subArray = [nums[i], nums[i + 1], nums[i + 2]]

            if (
                abs(subArray[0] - subArray[1]) <= k
                and abs(subArray[1] - subArray[2]) <= k
                and abs(subArray[0] - subArray[2]) <= k
            ):
                result.append(subArray)
            else:
                return []

        return result