class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
        Searches for an integer target in an m x n sorted matrix matrix.
        Returns True if target is found, False otherwise.
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
    
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
    
        return False
