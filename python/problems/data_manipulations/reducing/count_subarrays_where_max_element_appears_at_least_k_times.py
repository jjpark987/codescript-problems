#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        res = start = max_count = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_count += 1
            while max_count == k:
                if nums[start] == max_element:
                    max_count -= 1
                start += 1
            res += start
        return res

'''
category: data manipulations
subcategory: reducing
difficulty: medium
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Count Subarrays Where Max Element Appears at Least K Times

description:
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''