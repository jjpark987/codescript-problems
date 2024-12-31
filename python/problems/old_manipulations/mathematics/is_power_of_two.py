#!/usr/bin/env python3

# from typing import Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(n), space: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            ans = 2 ** i

            if ans == n:
                return True
            
        return False

print(Solution().isPowerOfTwo(1))
print('Expected: True')
print(Solution().isPowerOfTwo(3))
print('Expected: False')

"""
category: manipulations
subcategory: mathematics
difficulty: easy
image_url_e1: None
image_url_e2: None
title: Power of Two

description:
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""