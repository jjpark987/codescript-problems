#!/usr/bin/env python3

from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        points = 0
        
        for idx, q in sorted_queries:
            while heap and heap[0][0] < q:
                val, r, c = heapq.heappop(heap)
                points += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            res[idx] = points

        return res

'''
category: data manipulations
subcategory: reducing
difficulty: hard
image_path_e1: maximum_number_of_points_from_grid_queries_e1.png
image_path_e2: maximum_number_of_points_from_grid_queries_e2.png
image_path_e3: none
title: Maximum Number of Points From Grid Queries

description:
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
'''