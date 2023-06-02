class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        B = [list(row) for row in zip(*grid)]
        count = 0
        for i in grid:
            for j in B:
                if i== j:
                    count+=1
        return count

        