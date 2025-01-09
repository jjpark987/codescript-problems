#!/usr/bin/env python3

from typing import List
from collections import defaultdict

# time: O(nlog(n)), space: O(1)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def count_pairs_with_max_distance(max_dist):
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_dist:
                    j += 1
                count += j - i - 1
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count_pairs_with_max_distance(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left

print(Solution().smallestDistancePair(nums = [1,3,1], k = 1))
print('0')
print(Solution().smallestDistancePair(nums = [1,1,1], k = 2))
print('0')
print(Solution().smallestDistancePair(nums = [1,6,1], k = 3))
print('5')
print(Solution().smallestDistancePair(nums = [9,10,7,10,6,1,5,4,9,8], k = 18))
print('2')

"""
category: combinatorics
subcategory: counting
difficulty: hard
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Find K-th Smallest Pair Distance

description:
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""