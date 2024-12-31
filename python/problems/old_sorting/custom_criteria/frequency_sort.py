#!/usr/bin/env python3

from typing import List, Counter

# time: O(nlog(n)), space: O(n)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict(Counter(nums))

        sorted_freq = sorted(freq.items(), key=lambda item: (item[1], -item[0]))

        result = [num for num, freq in sorted_freq for _ in range(freq)]

        return result

print(Solution().frequencySort([1,1,2,2,2,3]))
print('Expected: [3,1,1,2,2,2]')
print(Solution().frequencySort([2,3,1,3,2]))
print('Expected: [1,3,3,2,2]')
print(Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1]))
print('Expected: [5,-1,4,4,-6,-6,1,1,1]')

"""
category: sorting
subcategory: custom criteria
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Sort Array by Increasing Frequency

description:
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""