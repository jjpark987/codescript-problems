#!/usr/bin/env python3

from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def higher_num(a, b):
            if int(a + b) > int(b + a):
                return -1
            elif int(b + a) > int(a + b):
                return 1
            else:
                return 0
            
        nums.sort(key=cmp_to_key(higher_num))

        return str(int(''.join(nums)))

"""
category: data manipulations
subcategory: reformatting
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