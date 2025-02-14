#!/usr/bin/env python3

from typing import List

# time: O(n + q), space: O(n)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n  # Prefix array to count special pairs

        # Build the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0):
                prefix[i] += 1

        result = []  # Result list

        # Process each query
        for left, right in queries:
            special_count = prefix[right] - (prefix[left] if left > 0 else 0)
            result.append(special_count == 0)

        return result

"""
category: data manipulations
subcategory: reducing
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Special Array II

description:
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""