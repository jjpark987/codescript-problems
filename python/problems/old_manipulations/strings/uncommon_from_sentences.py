#!/usr/bin/env python3

from typing import List

# time: O(n), space: O(n)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        results = {}

        def check_words(s):
            for w in s.split():
                if w not in results:
                    results[w] = True
                else:
                    results[w] = False

        check_words(s1)
        check_words(s2)

        return [key for key, value in results.items() if value]

print(Solution().uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print('["sweet","sour"]')
print(Solution().uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
print('["banana"]')

"""
category: manipulations
subcategory: strings
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Uncommon Words from Two Sentences

description:
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""