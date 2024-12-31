#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end_of_word = True

    def search(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.is_end_of_word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def findShortedPrefix(self, word):
        curr = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return word
            curr = curr.children[index]
            if curr.is_end_of_word:
                return word[:i + 1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        tokens = sentence.split()
        result = []
        for token in tokens:
            prefix = trie.findShortedPrefix(token)
            result.append(prefix)
        return ' '.join(result)

print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
print('Expected: "the cat was rat by the bat"')
print(Solution().replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
print('Expected: "a a b c"')
print(Solution().replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery"))
print('Expected: "the cat was rat by the bat"')

"""
category: manipulations
subcategory: strings
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Longest Palindrome

description:
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""