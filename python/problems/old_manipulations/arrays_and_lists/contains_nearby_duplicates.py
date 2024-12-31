#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()

        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            
            nums_set.add(nums[i])

            if len(nums_set) > k:
                nums_set.remove(nums[i - k])

        return False

        # if len(set(nums)) == len(nums):
        #     return False
        
        # i, j = 0, min(k + 1, len(nums))

        # while j <= len(nums):
        #     if len(set(nums[i:j])) != len(nums[i:j]):
        #         return True
        #     i += 1
        #     j += 1

        # return False

print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print('Expected: True')
print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print('Expected: True')
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print('Expected: False')

"""
category: manipulations
subcategory: arrays and lists
difficulty: easy
image_url_e1: None
image_url_e2: None
title: Contains Duplicate II

description:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""