#!/usr/bin/env python3

from typing import List

# time: O(3^n), space: O(3^n)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result: List[int] = []

        for i in range(len(expression)):
            op = expression[i]
            if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                left_res = self.diffWaysToCompute(expression[:i])
                right_res = self.diffWaysToCompute(expression[i + 1:])

                for l in left_res:
                    for r in right_res:
                        if op == '+':
                            result.append(int(l) + int(r))
                        elif op == '-':
                            result.append(int(l) - int(r))
                        else:
                            result.append(int(l) * int(r))

        if len(result) == 0:
            result.append(int(expression))

        return result

print(Solution().diffWaysToCompute(expression = "2-1-1"))
print('[0,2]')
print(Solution().diffWaysToCompute(expression = "2*3-4*5"))
print('[-34,-14,-10,-10,10]')

"""
category: manipulations
subcategory: strings
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Different Ways to Add Parentheses

description:
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
"""