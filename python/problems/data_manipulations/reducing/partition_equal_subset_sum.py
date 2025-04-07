#!/usr/bin/env python3

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        if target in nums:
            return True

        nums.sort(reverse=True)

        memo = {}
        def dfs(i, target):
            if target == 0:
                return True
            if i < 0 or target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            take = dfs(i - 1, target - nums[i])
            skip = dfs(i - 1, target)
            
            memo[(i, target)] = take or skip
            return memo[(i, target)]
        
        return dfs(len(nums) - 1, target)

'''
category: data manipulations
subcategory: reducing
difficulty: medium
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Partition Equal Subset Sum

description:
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''