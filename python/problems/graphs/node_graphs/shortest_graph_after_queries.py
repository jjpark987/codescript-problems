#!/usr/bin/env python3

from collections import deque
from typing import List

# time: O(n), space: O(n)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs():
            q = deque()
            q.append((0, 0))
            visited = set()
            visited.add((0, 0))

            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        q.append((neighbor, length + 1))
                        visited.add(neighbor)

        adj = [[i + 1] for i in range(n - 1)]
        res = []

        for start, end in queries:
            adj[start].append(end)
            res.append(bfs())

        return res

"""
category: graphs
subcategory: node graphs
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Shortest Distance After Road Addition Queries I

description:
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:



After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:



After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.



After the addition of the road from 0 to 2, the length of the shortest path remains 1.

 

Constraints:

3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
There are no repeated roads among the queries.
"""