#!/usr/bin/env python3

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            return [i for i in range(n + 1) if is_prime[i]]

        primes = [x for x in sieve(right) if x in range(left, right + 1)]
        n = len(primes)
        if n < 2:
            return [-1, -1]
        elif n == 2:
            return [primes[0], primes[1]]

        res = [0, 0]
        diff = float('inf')
        i, j = 0, 1

        while j < n:
            if primes[j] - primes[i] < diff:
                res = [primes[i], primes[j]]
                diff = primes[j] - primes[i]
            i += 1
            j += 1
            
        return res

'''
category: data manipulations
subcategory: reducing
difficulty: medium
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Closest Prime Numbers in Range

description:
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
'''