#!/usr/bin/env python

import ipdb
# from typing import List
# from functools import reduce
from collections import deque, defaultdict

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        stack = deque()
        result = ''

        for i, char in enumerate(word):
            stack.append(char)

            if char == ch:
                for _ in range(len(stack)):
                    result += stack.pop()
                
                result += word[i + 1:]

                break
        
        return result
    
        # i = word.find(ch)
        # if i != -1:
        #     return word[:i+1][::-1] + word[i+1:]
        # return word

print(Solution().reversePrefix(word = 'abcdefd', ch = 'd'))

"""
category: data manipulations
subcategory: reformatting
difficulty: easy
image_path_e1: None
image_path_e2: None
title: Reverse Prefix of Word

description:
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".
 

Constraints:

1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
"""
