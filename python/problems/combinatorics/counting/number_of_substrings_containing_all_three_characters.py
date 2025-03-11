#!/usr/bin/env python3

# from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while all(count[c] > 0 for c in 'abc'):
                res += len(s) - r 
                count[s[l]] -= 1 
                l += 1 

        return res

'''
category: combinatorics
subcategory: counting
difficulty: medium
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Number of Substrings Containing All Three Characters

description:
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''