#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(n: str):
            res = ''
            count = 0
            val = n[0]
            for i in range(len(n)):
                cur = n[i]
                if cur == val:
                    count += 1
                else:
                    res += f'{str(count)}' + val
                    val = cur
                    count = 1
            res += f'{str(count)}' + val
            return res

        res = '1'

        for _ in range(n - 1):
            res = rle(res)

        return res

'''
category: data manipulations
subcategory: reformatting
difficulty: medium
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Count and Say

description:
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
'''