from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        rows_to_zero = [False] * m
        cols_to_zero = [False] * n
        
        # First pass to find all rows and columns that should be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero[i] = True
                    cols_to_zero[j] = True
        
        # Zero out rows
        for i in range(m):
            if rows_to_zero[i]:
                for j in range(n):
                    matrix[i][j] = 0
        
        # Zero out columns
        for j in range(n):
            if cols_to_zero[j]:
                for i in range(m):
                    matrix[i][j] = 0
    
if __name__ == "__main__":
    matrix = [[1, 0, 1], [1, 1, 1], [1, -2, 1]]
    solution = Solution()  # Create an instance of Solution
    solution.setZeroes(matrix)  # Modify the matrix in place
    
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()


        