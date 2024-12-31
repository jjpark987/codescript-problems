#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go through list, doubling each node and handling carry
        prev, curr, carry, new_head = None, head, 0, None
        
        while curr:
            result = curr.val * 2 + carry
            curr.val = result % 10
            carry = result // 10

            if carry > 0 and prev == None:
                new_head = ListNode(carry)
                new_head.next = curr
                carry = 0
            elif carry > 0:
                prev.val += carry
                carry = 0

            prev, curr = curr, curr.next
        
        return new_head or head

        # # helper function to reverse linked list
        # def reverse_list(prev, curr):
        #     curr.next, prev, curr = prev, curr, curr.next
        #     return prev, curr

        # # helper function to double values and return carry
        # def double_node(node, carry) -> int:
        #     result = node.val * 2 + carry
        #     node.val = result % 10
        #     return result // 10

        # # reverse head as prev
        # prev, curr = None, head
        # while curr:
        #     prev, curr = reverse_list(prev, curr)

        # # change node value and save carry
        # carry = double_node(prev, 0)

        # # go through the list, changing its values and reversing its direction
        # curr, prev.next = prev.next, None
        # while curr:
        #     carry = double_node(curr, carry)
        #     prev, curr = reverse_list(prev, curr)

        # # create new node if carry is not zero
        # if carry:
        #     new_head, new_head.next = ListNode(carry), prev
        #     return new_head
        
        # return prev

test = ListNode(9)
test.next = ListNode(9)
test.next.next = ListNode(9)

print(Solution().doubleIt(head=test))
print('Expected output: [1, 9, 9, 8]')

"""
category: linked lists
subcategory: singly
difficulty: medium
image_url_e1: /python/images/double_it_e1.png
image_url_e2: /python/images/double_it_e2.png
title: Double a Number Represented as a Linked List

description:
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:
/python/images/double_it_e1.png

Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:
/python/images/double_it_e2.png

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""