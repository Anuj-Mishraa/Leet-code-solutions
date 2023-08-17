from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Store the number of rows and columns
        m, n = len(mat), len(mat[0])
        
        # Create a queue to use for BFS
        q = deque()
        
        # Iterate through each value in the matrix
        for r in range(m):
            for c in range(n):
                # If the current value is 0, then set the distance to 0
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                # Else set the value to infinity
                else:
                    mat[r][c] = float('inf')
                    
        # Directions we can explore (up, down, left, right)
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        # While the queue holds elements
        while q:
            # Retrieve row, col, and distance from queue
            x, y, distance = q.popleft()
            
            # Iterate through neighboring cells
            for d in directions:
                # Update row and column coordinates
                neighbor_r = x + d[0] 
                neighbor_c = y + d[1]
                
                # Check to make sure they're within the boundaries of the matrix
                if 0 <= neighbor_r < m and 0 <= neighbor_c < n:
                    # If the neighbor's distance is larger than the current cell's + 1, set it to current + 1 and add to queue
                    if mat[neighbor_r][neighbor_c] > distance + 1:
                        mat[neighbor_r][neighbor_c] = distance + 1
                        q.append((neighbor_r, neighbor_c, distance + 1))
        
        return mat
