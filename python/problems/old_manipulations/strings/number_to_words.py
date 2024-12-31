#!/usr/bin/env python3

# time: O(n), space: O(n)
class Solution:
    def numberToWords(self, num: int) -> str:
        digits_map = {
            '0': 'Zero',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
            '20': 'Twenty',
            '30': 'Thirty',
            '40': 'Forty',
            '50': 'Fifty',
            '60': 'Sixty',
            '70': 'Seventy',
            '80': 'Eighty',
            '90': 'Ninety',
        }

        def convert_two(num: str) -> str:
            n = int(num)

            if n < 20 or num[1] == '0':
                return digits_map[num]
            else:
                return digits_map[num[0] + '0'] + ' ' + digits_map[num[1]]
            
        def convert_three(num: str) -> str:
            n = int(num)

            if n < 100:
                return convert_two(num)
            else:
                result = digits_map[num[0]] + ' Hundred'

                if num[1] == '0' and num[2] == '0':
                    return result
                
                result += ' ' + convert_two(str(n % 100))

                return result

        s = str(num)

        if s in digits_map:
            return digits_map[s]

        l = len(s)
        groups = []

        for i in range(l, 0, -3):
            start_i = max(0, i - 3)
            groups.append(s[start_i:i])

        result = []

        for index, group in enumerate(groups):
            if index == 0:
                if group != '000':
                    result.append(convert_three(str(int(group))))
            elif index == 1:
                if group != '000':
                    result.append(convert_three(str(int(group))) + ' Thousand')
            elif index == 2:
                if group != '000':
                    result.append(convert_three(str(int(group))) + ' Million')
            else:
                if group != '000':
                    result.append(convert_three(group) + ' Billion')

        result.reverse()

        return ' '.join(result)

print(Solution().numberToWords(20001000000))
print('Expected: "One Hundred Twenty Three"')
print(Solution().numberToWords(12345))
print('Expected: "Twelve Thousand Three Hundred Forty Five"')
print(Solution().numberToWords(1234567))
print('Expected: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"')

"""
category: manipulations
subcategory: strings
difficulty: hard
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Integer to English Words

description:
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""