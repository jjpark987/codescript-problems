#!/usr/bin/env python3

from typing import List

# time: O(n), space: O(1)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowest = arrays[0][0]
        highest = arrays[0][-1]
        result = float('-inf')

        for i in range(1, len(arrays)):
            result = max(result, highest - arrays[i][0], arrays[i][-1] - lowest)

            lowest = min(lowest, arrays[i][0])
            highest = max(highest, arrays[i][-1])

        return result

print(Solution().maxDistance([[1,2,3],[4,5],[1,2,3]]))
print('4')
print(Solution().maxDistance([[1],[1]]))
print('0')
print(Solution().maxDistance([[-2],[-3,-2,1]]))
print('3')

"""
category: optimizations
subcategory: maximization
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Maximum Distance in Arrays

description:
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
 

Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
"""