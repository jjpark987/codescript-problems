#!/usr/bin/env python

# import ipdb
# from typing import List
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(n):
            if n in cache:
                return cache[n]

            if n == 0 or n == 1:
                return 1
            
            cache[n] = climb(n - 1) + climb(n - 2)
            
            return cache[n]
        
        return climb(n)
    
        # if n == 0 or n == 1:
        #     return 1
        
        # prev, curr = 1, 1

        # for i in range(2, n+1):
        #     temp = curr
        #     curr = prev + curr
        #     prev = temp
        
        # return curr

print(Solution().climbStairs(n=2))
print(Solution().climbStairs(n=3))
print(Solution().climbStairs(n=5))

"""
category: combinatorics
subcategory: counting
difficulty: easy
image_url_e1: None
image_url_e2: None
title: Climbing Stairs


description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""