#!/usr/bin/env python3

# time: O(n), space: O(n)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, first, second, points_value):
            stack = []
            points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    points += points_value
                else:
                    stack.append(char)
            remaining = ''.join(stack)
            return remaining, points
        
        # Determine the order based on the points
        if x >= y:
            s, points = remove_and_score(s, 'a', 'b', x)
            s, additional_points = remove_and_score(s, 'b', 'a', y)
            points += additional_points
        else:
            s, points = remove_and_score(s, 'b', 'a', y)
            s, additional_points = remove_and_score(s, 'a', 'b', x)
            points += additional_points
        
        return points

print(Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
print('Expected: 19')
print(Solution().maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))
print('Expected: 20')

"""
category: optimization
subcategory: strings
difficulty: medium
image_path_e1: None
image_path_e2: None
title: Maximum Score From Removing Substrings

description:
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""