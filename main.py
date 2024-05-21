#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import deque, defaultdict
from functools import reduce

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # iterate range(2**len(nums)) times, each one representing a subset
        for i in range(2**len(nums)):
            subset = []

            # to find each subset, we iterate through the list of ints
            for j in range(len(nums)):
                # starting from j = 0 (the right most bit), we shift the bits to the right
                # this allows us to compare the jth bit of bin(i) because it is now in the right most position
                # we check if the bit in the right most position is 1
                # if it is, we add the element in index j into the subset
                if (i >> j) & 1:
                    subset.append(nums[j])

            result.append(subset)

        return result
    
        # RECURSIVE BACKTRACKING

        # def backtrack(start, path):
        #     result.append(path)
        #     for i in range(start, len(nums)):
        #         backtrack(i + 1, path + [nums[i]])

        # result = []
        # backtrack(0, [])
        # return result


print(Solution().subsets([1,2,3]))
print('Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]')

"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""