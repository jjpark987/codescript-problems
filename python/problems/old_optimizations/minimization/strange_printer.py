#!/usr/bin/env python3

from typing import List

# time: O(n^3), space: O(n^2)
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        
        return dp[0][n - 1]

print(Solution().strangePrinter(s = "aaabbb"))
print('2')
print(Solution().strangePrinter(s = "aba"))
print('2')
print(Solution().strangePrinter(s = "ababbbcba"))
print('4')

"""
category: optimizations
subcategory: minimization
difficulty: hard
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Strange Printer

description:
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""