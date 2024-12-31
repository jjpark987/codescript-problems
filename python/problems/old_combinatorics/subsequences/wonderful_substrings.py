#!/usr/bin/env python

import ipdb
# from typing import List
# from functools import reduce
from collections import deque, defaultdict

class Solution(object):
    def wonderfulSubstrings(self, word):
        count = defaultdict(int)
        count[0] = 1
        result = 0
        bitmask = 0

        for char in word:
            char_index = ord(char) - ord('a')
            bitmask ^= 1 << char_index
            result += count[bitmask]

            for i in range(10):
                result += count[bitmask ^ (1 << i)]

            count[bitmask] += 1
        
        return result

print(Solution().wonderfulSubstrings(word='aba'))

"""
category: combinatorics
subcategory: subsequences
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Number of Wonderful Substrings

description:
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""
