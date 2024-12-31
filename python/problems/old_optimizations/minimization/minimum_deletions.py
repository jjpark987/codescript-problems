#!/usr/bin/env python3

from typing import List

# time: O(n), space: O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        min_operations = 0
        
        for c in s:
            if c == 'a':
                min_operations = min(min_operations + 1, b_count)
            else:
                b_count += 1

        return min_operations

print(Solution().minimumDeletions("aababbab"))
print('Expected: 2')
print(Solution().minimumDeletions("bbaaaaabb"))
print('Expected: 2')

"""
category: optimizations
subcategory: minimizations
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Minimum Deletions to Make String Balanced

description:
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
"""