#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]

        for n in nums:
            freq[n] += 1

        count = 0

        for i in range(3):
            nums[count:count + freq[i]] = [i] * freq[i]
            count += freq[i]

print(Solution().sortColors([2,0,2,1,1,0]))
print('Expected: [0,0,1,1,2,2]')
print(Solution().sortColors([2,0,1]))
print('Expected: [0,1,2]')
print(Solution().sortColors([1,2,0]))
print('Expected: [0,1,2]')

"""
category: sorting
subcategory: custom criteria
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Sort Colors

description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""