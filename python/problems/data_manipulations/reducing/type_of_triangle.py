#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter, deque, defaultdict

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)

        if a + b <= c:
            return 'none'
        
        counter = Counter(nums)
        n = len(counter)

        if n == 1:
            return 'equilateral'
        elif n == 2:
            return 'isosceles'
        else:
            return 'scalene'
        
'''
category: data manipulations
subcategory: reducing
difficulty: easy
image_path_e1: none
image_path_e2: none
image_path_e3: none
title: Type of Triangle

description:
You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
 

Constraints:

nums.length == 3
1 <= nums[i] <= 100
'''