#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import deque, defaultdict
from functools import reduce

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            
            include = dfs(index + 1, current_xor ^ nums[index])
            exclude = dfs(index + 1, current_xor)

            return include + exclude
        
        return dfs(0, 0)
        
        # BRUTE FORCE
        # xor_sum = 0

        # # create for loop that starts from i = 1 and ends in 2^len(nums) - 1
        # for i in range(1, 2**len(nums)):
        #     # convert i into binary representation
        #     binary = bin(i)[2:]

        #     # each index in binary represenation represents the element in nums[index]
        #     # if the index is set, include the element in nums[index] in the subset
        #     temp = []

        #     for index, bit in enumerate(binary[::-1]):
        #         if bit == '1':
        #             temp.append(nums[index])

        #     # for each subset created, perform XOR
        #     if len(temp) == 1:
        #         temp = temp[0]
        #     else:
        #         temp = reduce(lambda x, y: x ^ y, temp)

        #     xor_sum += temp
        
        # # return sum of subsets
        # return xor_sum


print(Solution().subsetXORSum([5,1,6]))
print('Expected: 28')

"""
category: combinatorics
subcategory: subsets
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Sum of All Subset XOR Totals

description:
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
Example 3:

Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.
 

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
"""