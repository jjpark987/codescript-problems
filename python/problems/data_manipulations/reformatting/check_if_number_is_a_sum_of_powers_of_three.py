#!/usr/bin/env python3

# from typing import List

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        visited = set()
        def subtract(n):
            if n == 0:
                return True
            if n < 0:
                return False
            power = 1
            while power * 3 <= n:
                power *= 3
            if power in visited:
                return False
            visited.add(power)
            remainder = n - power
            return subtract(remainder)

        return subtract(n)

'''
category: data manipulations
subcategory: reformatting
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Check if Number is a Sum of Powers of Three

description:
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
'''