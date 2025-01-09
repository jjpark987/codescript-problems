#!/usr/bin/env python3

from typing import List
from math import isqrt
from heapq import heapify, heappop, heappush

# time: O(n + klogn), space: O(n)
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts)
        x, i = 2, 0

        while i < k and x > 1:
            # print(gifts)
            x = -heappop(gifts)
            # print(x)
            heappush(gifts, -isqrt(x))
            # print(gifts)
            i += 1

        return -sum(gifts)

"""
category: optimizations
subcategory: structures
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Take Gifts From the Richest Pile

description:
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

 

Example 1:

Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
Example 2:

Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation: 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4.
 

Constraints:

1 <= gifts.length <= 103
1 <= gifts[i] <= 109
1 <= k <= 103
"""