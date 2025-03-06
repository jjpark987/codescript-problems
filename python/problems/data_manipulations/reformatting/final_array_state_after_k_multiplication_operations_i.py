#!/usr/bin/env python3

from typing import List
from heapq import heapify, heappop, heappush

# time: O(klogn + nlogn), space: O(n)
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_tuple = [(x, i) for i, x in enumerate(nums)]
        heapify(nums_tuple)

        for _ in range(k):
            value, index = heappop(nums_tuple)
            heappush(nums_tuple, (value * multiplier, index))

        nums_tuple.sort(key=lambda item: item[1])
        return [item[0] for item in nums_tuple]

"""
category: data manipulations
subcategory: reformatting
difficulty: easy
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Final Array State After K Multiplication Operations I

description:
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

 

Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
Example 2:

Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:

Operation	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5
"""