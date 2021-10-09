# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #pop first row
        #pop last col
        #pop last row
        #pop first col

        ans = []

        try: 
            while matrix != []:
                temp = matrix.pop(0)#[:, 0]
                ans += temp

                for i, mat in enumerate(matrix):
                    ans += [mat.pop(-1)]

                temp = matrix.pop(-1)
                ans += temp[::-1]

                for i, mat in enumerate(matrix[::-1]):
                    ans += [mat.pop(0)]
                    
        except Exception as e:
            print(e)

        return ans