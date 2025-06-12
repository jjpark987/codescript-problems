#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(1, len(nums)):
            res = max(res, abs(nums[i] - nums[i - 1]))
        res = max(res, abs(nums[0] - nums[-1]))
        return res

'''
category: data manipulations
subcategory: reducing
difficulty: easy
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Maximum Difference Between Adjacent Elements in a Circular Array

description:
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100
'''