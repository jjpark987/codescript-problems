#!/usr/bin/env python3

from typing import List
from collections import Counter

# time: O(n), space: O(n)
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        for s in count:
            if count[s] == 1:
                k -= 1

                if k == 0:
                    return s
                
        return ''

print(Solution().kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
print('Expected: "a"')
print(Solution().kthDistinct(arr = ["aaa","aa","a"], k = 1))
print('Expected: "aaa"')

"""
category: searching
subcategory: value matching
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Kth Distinct String in an Array

description:
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
"""