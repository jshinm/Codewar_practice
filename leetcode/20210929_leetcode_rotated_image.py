# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Example 3:

# Input: matrix = [[1]]
# Output: [[1]]
# Example 4:

# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
 

# Constraints:

# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# the common matrix rotation solutions are:
# clockwise: vertical inverse then diagonal swap 
# counter-clockwise: left-right inverse then diagonal swap

from typing import List

class Solution:
    def rotate_I(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # rotate then move inward
        # 6 -> 4 -> 2; matrix reduces by two as moving inward
        
        n = len(matrix)
        
        def turn(l, i, mat):
            #l: top, left
            #r: bottom, right
            #i: left pointer
            #j: right pointer
            
            r = -(l + 1)
            j = -(i + 1)
            
            # right : mat[i][r]
            # left : mat[j][l]
            # top : mat[l][i]
            # bottom : mat[r][j]
            
            #top to right
            temp = mat[i][r] #temp <- right
            mat[i][r] = mat[l][i] #right <- top
            
            #right to bottom
            temp2 = mat[r][j]  #temp2 <- bottom
            mat[r][j] = temp #bottom <- right
            
            #bottom to left
            temp = mat[j][l] #temp <- left
            mat[j][l] = temp2 #left <- bottom
            
            #left to top
            mat[l][i] = temp #top <- left
        
        dim = n
        d = 0
        
        while dim > 1: #condition for the inner most matrix
            #n-d to move right column to left by one column
            #starting from d moves left column to right by one column
            #thus reducing matrix by 2
            
            for i in range(d, n-d-1): 
                turn(d, i, matrix)
                # print(d, i)
            
            dim -= 2 #matrix reduce by size of 2
            d += 1 #each movement towards inner matrix initiates at n+1

    def rotate_II(self, matrix: List[List[int]]) -> None:
        # vertical reverse followed by diagonal swap method
        
        n = len(matrix)
        
        #vertical reverse
        for i in range(int(n/2)):
            matrix[i], matrix[-(i+1)] = matrix[-(i+1)], matrix[i]
        
        #diagonal swap
        for i in range(n):
            for j in range(i, n):
                if i != j: #no need to swap itself
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]