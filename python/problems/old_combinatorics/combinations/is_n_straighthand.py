#!/usr/bin/env python3

import ipdb
from typing import List, Optional
from collections import Counter, deque, defaultdict
# from functools import reduce

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        sorted_keys = sorted(count.keys())
        print(sorted_keys)
        print(count)
        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]

                for i in range(key, key + groupSize):
                    ipdb.set_trace()
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
                    ipdb.set_trace()
        
        return True

print(Solution().isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
print('Expected: True')
# print(Solution().isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))
# print('Expected: False')

"""
category: combinatorics
subcategory: combinations
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Hand of Straights

description:
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.


Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""