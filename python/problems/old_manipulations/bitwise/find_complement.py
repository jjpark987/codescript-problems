#!/usr/bin/env python3

# time: O(1), space: O(1)
class Solution:
    def findComplement(self, num: int) -> int:
        # find bit_length
        bit_length = num.bit_length()
        
        # calculate bitmask using bit_length
        # this bitmask is binary of all 1s with length of bit_length
        mask = (1 << bit_length) - 1
        
        # use exclusive or (xor) to flip binary of num using bitmask
        return num ^ mask

print(Solution().findComplement(5))
print('2')
print(Solution().findComplement(1))
print('0')

"""
category: manipulations
subcategory: bitwise
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Number Complement

description:
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
"""