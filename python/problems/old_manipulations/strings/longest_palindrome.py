#!/usr/bin/env python3

import ipdb
# from typing import List, Optional
# from collections import deque, defaultdict
# from functools import reduce

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # map all char in s, counting their frequency
        tally = {}
        odds = 0
        for char in s:
            if char in tally:
                tally[char] += 1
            else:
                tally[char] = 1
            
        # for each key, find number of char that appear odd times, (odds)
        odds = sum(1 for char in tally if tally[char] % 2 == 1)

        # return length of s and subtract odds - 1
        if odds > 1:
            return len(s) - odds + 1

        return len(s)

print(Solution().longestPalindrome("abccccdd"))
print('Expected: 7')
print(Solution().longestPalindrome("a"))
print('Expected: 1')

"""
category: manipulations
subcategory: strings
difficulty: easy
image_url_e1: None
image_url_e2: None
title: Longest Palindrome

description:
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""