#!/usr/bin/env python3

from typing import List

# time: O(rows * cols), space: O(rows * cols)
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        move_cols = True
        increment = 1
        direction = 1
        current = [rStart, cStart]
        result = [current]

        while len(result) < rows * cols:
            if move_cols:
                for _ in range(increment):
                    current = [current[0], current[1] + direction]
                    
                    if current[0] in range(rows) and current[1] in range(cols):
                        result.append(current)

                move_cols = False
                
            else:
                for _ in range(increment):
                    current = [current[0] + direction, current[1]]
                    
                    if current[0] in range(rows) and current[1] in range(cols):
                        result.append(current)

                move_cols = True
                increment += 1
                direction *= -1

        return result

print(Solution().spiralMatrixIII(rows = 1, cols = 4, rStart = 0, cStart = 0))
print('[[0,0],[0,1],[0,2],[0,3]]')
print(Solution().spiralMatrixIII(rows = 5, cols = 6, rStart = 1, cStart = 4))
print('[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]')

"""
category: data manipulations
subcategory: generating
difficulty: medium
image_url_e1: /python/images/spiral_matrix_iii_e1.png
image_url_e2: /python/images/spiral_matrix_iii_e1.png
image_url_e3: none
title: Spiral Matrix III

description:
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""