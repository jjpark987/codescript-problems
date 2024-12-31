#!/usr/bin/env python3

from typing import List

# time: O(nlog(n)), space: O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            sorted_left = merge_sort(left)
            sorted_right = merge_sort(right)

            return merge(sorted_left, sorted_right)

        def merge(left, right):
            result = []
            left_i = 0
            right_i = 0

            while left_i < len(left) and right_i < len(right):
                if left[left_i] <= right[right_i]:
                    result.append(left[left_i])
                    left_i += 1
                else:
                    result.append(right[right_i])
                    right_i += 1

            while left_i < len(left):
                result.append(left[left_i])
                left_i += 1

            while right_i < len(right):
                result.append(right[right_i])
                right_i += 1

            return result
        
        return merge_sort(nums)
                
print(Solution().sortArray([5,2,3,1]))
print('Expected: [1,2,3,5]')
# print(Solution().sortArray([5,1,1,2,0,0]))
# print('Expected: [0,0,1,1,2,5]')

"""
category: sorting
subcategory: custom criteria
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Sort an Array

description:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""