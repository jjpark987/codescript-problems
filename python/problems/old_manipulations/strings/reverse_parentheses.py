#!/usr/bin/env python3

from typing import List
from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(n), space: O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        i_pairs = [0] * n
        stack_start_i = deque()

        for i in range(n):
            c = s[i]

            if c == '(':
                stack_start_i.append(i)
            elif c == ')':
                start_i = stack_start_i.pop()
                i_pairs[i] = start_i
                i_pairs[start_i] = i

        result = []
        cur_i = 0
        cur_dir = 1

        while cur_i < n:
            c = s[cur_i]

            if c in '()':
                cur_i = i_pairs[cur_i]
                cur_dir *= -1
            else:
                result.append(c)
            
            cur_i += cur_dir

        return ''.join(result)

# print(Solution().reverseParentheses("(abcd)"))
# print('Expected: "dcba"')
# print(Solution().reverseParentheses("(u(love)i)"))
# print('Expected: "iloveu"')
# print(Solution().reverseParentheses("(ed(et(oc))el)"))
# print('Expected: "leetcode"')
print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
print('Expected: "apmnolkjihgfedcbq"')

"""
category: manipulations
subcategory: strings
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Reverse Substrings Between Each Pair of Parentheses

description:
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""