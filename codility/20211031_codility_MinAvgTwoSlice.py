# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # The goal is to find the starting position of a slice whose average is minimal
    # brute force is exaustive search which is O(N^2)
    minN = None
    idx = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            tmp = sum(A[i:j+1])/(j-i+1)
            tmp_list.append((i,j,tmp))

            if minN == None or minN > tmp:
                minN = tmp
                idx = i

    return idx

# Kadane's algorithm using 2/3 window
# https://stackoverflow.com/questions/21635397/min-average-two-slice-codility


# generalized solution without 2/3 window
# class Solution {
#     public int solution(int[] A) {
#         // write your code in Java SE 8
#             // write your code in Java SE 8

#     float avg = 0f;
#     int min_index = 0;
#     int P = 0;
#     //formula

#     float sums[] = new float[A.length ];

#     //suffix sums
#     int prefix = 0;
#     for (int i = 0; i < A.length; i += 1) {
#         prefix += A[i];
#         sums[i] += prefix;
#     }
#     float min_avg = Float.MAX_VALUE;
#     for (int i = 1; i < A.length; i++) {
#         avg = (sums[i] - sums[P] + A[P]) / (i - P + 1);
#         if (avg < min_avg) {
#             min_avg = avg;
#             min_index = P;
#         }
#             if (A[i] < min_avg) {
#             P = i;
#         }
#     }
#     return min_index;
# }
#     }