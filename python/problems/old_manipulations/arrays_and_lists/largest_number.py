#!/usr/bin/env python3

from typing import List
from functools import cmp_to_key

# time: O(n*log(n)), space: O(n)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            # Compare concatenated strings
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # equal
            
        # Turn all integers into strings
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        # Sort the list using custom function
        nums.sort(key=cmp_to_key(compare))

        # Concatenate the strings
        result = ''
        for n in nums:
            result += str(n)

        # If all values are 0s, return '0'
        if result[0] == '0':
            return '0'

        return result

# print(Solution().largestNumber(nums = [10,2]))
# print('210')
# print(Solution().largestNumber(nums = [3,30,34,5,9]))
# print('9534330')
print(Solution().largestNumber(nums = [0,0]))
print('0')

"""
category: manipulations
subcategory: arrays_and_lists
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Largest Number

description:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""