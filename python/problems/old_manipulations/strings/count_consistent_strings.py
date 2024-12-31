#!/usr/bin/env python3

from typing import List

# time: O(m * k), space: O(n)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_set = set(allowed)

        for word in words:
            for char in word:
                if char not in allowed_set:
                    break
            else:
                result += 1

        return result

print(Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print('2')
print(Solution().countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print('7')
print(Solution().countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
print('4')

"""
category: manipulations
subcategory: strings
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Count the Number of Consistent Strings

description:
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""