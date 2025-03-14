#!/usr/bin/env python

import ipdb
import functools

class Solution:
    def __init__(self):
        self.cache = {}

    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.cache[n]
    
    # @functools.cache
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1 or n == 2:
    #         return 1

    #     return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            
print(Solution().tribonacci(n=40))

"""
category: optimizations
subcategory: processes
difficulty: easy
image_path_e1: None
image_path_e2: None
title:  N-th Tribonacci Number

description:
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""