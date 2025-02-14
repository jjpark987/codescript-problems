#!/usr/bin/env python3

from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulus = {}
        for n in arr:
            m = n % k
            modulus[m] = modulus.get(m, 0) + 1

        for m in modulus:
            if m == 0:
                if modulus[m] % 2 != 0:
                    return False
            elif k / 2 == m:
                if modulus[m] % 2 != 0:
                    return False
            else:
                match = k - m
                if modulus.get(match, 0) != modulus[m]:
                    return False

        return True

"""
category: combinatorics
subcategory: counting
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Check If Array Pairs Are Divisible by k

description:
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
"""