# Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Constraints:
* m == matrix.length
* n == matrix[0].length
* 1 <= m, n <= 200
* -231 <= matrix[i][j] <= 231 - 1

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        1. linear search to find the coordinates of the zeroes
        2. get the list of rows and cols that needs to be zeroed
        3. change matrix in-place
        
        TC:O(M*N), SC:O(M+N)
        """
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        irow = []
        icol = []
        
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    irow.append(i)
                    icol.append(j)
          
        for i in set(irow):
            for j in range(ncol):
                matrix[i][j] = 0
                
        for i in set(icol):
            for j in range(nrow):
                matrix[j][i] = 0
```
