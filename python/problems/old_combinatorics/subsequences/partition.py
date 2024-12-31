#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import deque, defaultdict
# from functools import reduce

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # DYNAMIC PROGRAMMING

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, path + [s[start:end+1]])

        result = []
        backtrack(0, [])
        return result

        # RECURSIVE BACKTRACKING

        # # create helper method that checks if a string is palindrome
        # # utilize two-pointer method
        # def is_palindrome(s) -> bool:
        #     left = 0
        #     right = len(s) - 1
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True
        
        # # this helper method is the recursive function
        # def backtrack(start, path):
        #     # if the current index reaches the end of the string, that means the current path is valid
        #     if start == len(s):
        #         # append the current path (substring) to the result list
        #         result.append(path[:])
        #         return
        #     # iterate over all possible psotions from start + 1 to len(s)
        #     for end in range(start + 1, len(s) + 1):
        #         # for each end position, check if substring s[start:end] is palindrome
        #         if is_palindrome(s[start:end]):
        #             # if it is, recursively call backtrack with the updated start (end) and current path plus new palindrome substring
        #             backtrack(end, path + [s[start:end]])

        # result = []
        # backtrack(0, [])
        # return result


print(Solution().partition('aab'))
print('Expected: [["a","a","b"],["aa","b"]]')

"""
category: combinatorics
subcategory: subsequences
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Palindrome Partitioning

description:
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""