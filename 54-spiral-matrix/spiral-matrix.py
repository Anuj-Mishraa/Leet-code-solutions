class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = m-1
        top = 0
        bottom = n-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if left >right or top>bottom:
                break
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
        return ans
