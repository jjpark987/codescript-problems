#!/usr/bin/env python3

import ipdb
from typing import List, Optional
from collections import deque, defaultdict
# from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total_xor = 0

        for n in nums:
            total_xor ^= n

        group_one, group_two = 0, 0

        bit_pos_dif = 0

        while (total_xor >> bit_pos_dif) & 1 == 0:
            bit_pos_dif += 1

        for n in nums:
            if (n >> bit_pos_dif) & 1 == 1:
                group_one ^= n
            else:
                group_two ^= n

        return [group_one, group_two]
    
        # DICTIONARY MAP
        # tally = defaultdict(lambda: 1)
        # for i in nums:
        #     if i in tally:
        #         tally[i] += 1

        #     tally[i]
        # return [i for i in tally if tally[i] == 1]
        

print(Solution().singleNumber([1,2,1,3,2,5]))
print('Expected: [3,5]')
print(Solution().singleNumber([-1,0]))
print('Expected: [-1,0]')
print(Solution().singleNumber([0,1]))
print('Expected: [1,0]')

"""
category: manipulations
subcategory: bit
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Single Number III

description:
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""