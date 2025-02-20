#!/usr/bin/env python3

# from typing import List

import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    # get google docs data
    export_url = doc_url + '?format=html'
    response = requests.get(export_url)

    # parse contents
    soup = BeautifulSoup(response.text, 'html.parser')
    rendered_text = soup.get_text( strip=True)

    # obtain coordinates and value and store in dictionary
    coordinates = {}
    start = rendered_text.find('y-coordinate') + 12
    temp_x, temp_ch  = 0, ''
    max_x, max_y = 0, 0
    n = len(rendered_text)
    i = start

    while i < n:
        # capture x coordinate
        temp_x_str = ''

        while rendered_text[i].isdigit():
            temp_x_str += rendered_text[i]
            i += 1

        temp_x = int(temp_x_str)  
        max_x = max(max_x, temp_x)

        # capture character
        temp_ch = rendered_text[i]
        i += 1  

        # capture y coordintate
        if rendered_text[i].isdigit():
            temp_y = int(rendered_text[i])
            max_y = max(max_y, temp_y)
            coordinates[(temp_x, temp_y)] = temp_ch
        i += 1

    # print as a grid
    for y in range(max_y, -1, -1):
        row = []
        for x in range(max_x + 1):
            row.append(coordinates.get((x, y), ' '))
        print(''.join(row))

# Example Usage
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
decode_secret_message(doc_url)

'''
category: combinatorics
subcategory: generating
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Find Unique Binary String

description:
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ['01','10']
Output: '11'
Explanation: '11' does not appear in nums. '00' would also be correct.
Example 2:

Input: nums = ['00','01']
Output: '11'
Explanation: '11' does not appear in nums. '10' would also be correct.
Example 3:

Input: nums = ['111','011','001']
Output: '101'
Explanation: '101' does not appear in nums. '000', '010', '100', and '110' would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
'''