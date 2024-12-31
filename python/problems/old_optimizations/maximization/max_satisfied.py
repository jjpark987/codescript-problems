#!/usr/bin/env python3

from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(n), space: O(1)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result = -1 
        # total number of customers if we do not use any minutes
        total = sum((1 - grumpy[i]) * customers[i] for i in range(len(customers)))
        # total number of a subset (window) of customers assuming all grumpy[i] is 0
        window_all = 0
        # total number of a subset (window) of customers only if grumpy is 0
        window_partial = 0

        # for each customer
        for i in range(len(customers)):
            window_all += customers[i]
            window_partial += (1 - grumpy[i]) * customers[i]

            # if window size is or greater than minutes
            if i + 1 >= minutes:
                result = max(result, total - window_partial + window_all)
                left_i = i - minutes + 1
                window_all -= customers[left_i]
                window_partial -= ((1 - grumpy[left_i]) * (customers[left_i]))

        return result

print(Solution().maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
print('Expected: 16')
print(Solution().maxSatisfied(customers = [1], grumpy = [0], minutes = 1))
print('Expected: 1')

"""
category: optimizations
subcategory: maximization
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Grumpy Bookstore Owner

description:
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
"""