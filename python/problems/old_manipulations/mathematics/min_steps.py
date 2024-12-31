#!/usr/bin/env python3

# time: O(sqrt(n)), space: O(sqrt(n))
class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(n) -> bool:
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        def find_factors(n: int) -> list[tuple]:
            def find_sq_root(n: int) -> int:
                if n <= 0:
                    return -1

                low, high = 0, n
                while low <= high:
                    mid = (low + high) // 2
                    mid_sq = mid * mid
                    if mid_sq == n:
                        return mid
                    elif mid_sq <= n:
                        low = mid + 1
                    else:
                        high = mid - 1
                return high
            
            if n <= 0:
                return []
            
            factors = set()
            sq_root = find_sq_root(n)
            for i in range(2, sq_root + 1):
                if n % i == 0:
                    factors.add((n // i, i))
            return sorted(factors, key=lambda item: item[0])

        if n == 1:
            return 0
        if is_prime(n):
            return n
        if find_factors(n):
            highest_factor, multiplier = find_factors(n)[-1]
            return self.minSteps(highest_factor) + multiplier

print(Solution().minSteps(3))
print('3')
print(Solution().minSteps(1))
print('0')
print(Solution().minSteps(110))
print('18')

"""
category: manipulations
subcategory: mathematics
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Keys Keyboard

description:
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
"""