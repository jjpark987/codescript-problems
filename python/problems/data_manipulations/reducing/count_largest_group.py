#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()

        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            counter[key] += 1

        max_size = max(counter.values())
        count = sum([1 for v in counter.values() if v == max_size])

        return count
    
'''
category: data manipulations
subcategory: reducing
difficulty: easy
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Count Largest Group

description:
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
'''