class Solution:
    def rearrangeArray(self, nums):
        a, b, c = [], [], []

        # Separate positive and negative integers into two separate arrays
        for num in nums:
            if num > 0:
                a.append(num)
            else:
                b.append(num)

        # Interleave positive and negative integers while preserving their order
        count, c1, c2 = 0, 0, 0
        for num in nums:
            if count % 2 == 0:
                n = a[c1]
                c.append(n)
                c1 += 1
            else:
                n = b[c2]
                c.append(n)
                c2 += 1
            count += 1

        return c