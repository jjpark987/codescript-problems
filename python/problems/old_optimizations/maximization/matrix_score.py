#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # greedy
        m, n = len(grid), len(grid[0])
        score = (1 << (n - 1)) * m

        for j in range(1, n):
            val = 1 << (n - 1 - j)
            set_count = 0

            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    set_count += 1
            
            score += max(set_count, m - set_count) * val

        return score

print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
print('Expected: 39')

"""
category: optimizations
subcategory: maximization
difficulty: medium
image_url_e1: /python/images/matrix_score_e1.jpg
image_url_e2: None
title: Score After Flipping Matrix

description:
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:
/python/images/matrix_score_e1.jpg

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
"""