#!/usr/bin/env python3

# from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        if 0 in nums:
            zero_count = nums.count(0)
            n -= zero_count
            if n == 0:
                return 0
            nums = [n for n in nums if n != 0]
        
        first = nums[0]
        last = nums[-1]

        if first ^ last >= 0:
            return len(nums)

        high = n
        low = 0
        last_neg = 0

        while low < high:
            mid = (high + low) // 2
            cur = nums[mid]
            nex = nums[mid + 1]

            if cur ^ nex < 0:
                last_neg = mid
                break
            elif cur < 0:
                low = mid
            else:
                high = mid
        
        return max(last_neg + 1, n - last_neg - 1)

'''
category: data manipulations
subcategory: reducing
difficulty: easy
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Maximum Count of Positive Integer and Negative Integer

description:
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
'''