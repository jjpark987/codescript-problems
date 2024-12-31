#!/usr/bin/env python3

from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(n), space: O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            if num % 2 == 1:
                count += 1
            else:
                count = 0

            if count == 3:
                return True
            
        return False

print(Solution().threeConsecutiveOdds([2,6,4,1]))
print('Expected: False')
print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print('Expected: True')

"""
category: manipulations
subcategory: arrays and lists
difficulty: easy
image_url_e1: None
image_url_e2: None
title: Three Consecutive Odds

description:
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""