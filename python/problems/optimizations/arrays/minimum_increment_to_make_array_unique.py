#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(nlog(n)), space: O(1)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        curr_num = 0

        for n in nums:
            curr_num = max(curr_num, n)
            result += curr_num - n
            curr_num += 1

        return result

print(Solution().minIncrementForUnique([1,2,2]))
print('Expected: 1')
print(Solution().minIncrementForUnique([3,2,1,2,1,7]))
print('Expected: 6')

"""
category: optimizations
subcategory: arrays
difficulty: medium
image_path_e1: None
image_path_e2: None
title: Minimum Increment to Make Array Unique

description:
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""