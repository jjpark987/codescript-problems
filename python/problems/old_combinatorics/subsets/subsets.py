#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import deque, defaultdict
from functools import reduce

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(2**len(nums)):
            subset = []

            for j in range(len(nums)):
                if (i >> j) & 1:
                    subset.append(nums[j])

            result.append(subset)

        return result


print(Solution().subsets([1,2,3]))
print('Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]')

"""
category: combinatorics
subcategory: subsets
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Subsets

description:
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