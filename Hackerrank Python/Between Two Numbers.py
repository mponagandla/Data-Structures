#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
# [a,b] -> x ; x -> [c,d,e]

def getTotalX(a, b):
    # Write your code here
    between_nums = []
    new_items = []
    flag = {}
    for num in range(a[0], b[1]+1):
        if num not in flag:
            flag[num] = 1
        for item in a:
            if num % item != 0:
                flag[item] = 0
            elif num % item == 0:
                new_items.append(num)
                flag[item] = 1

    for num in between_nums:
        flag = 1
        for item in b:
            if flag[num]:
                if item % num != 0:
                    flag[num] = 0
                elif item % num == 0 and num not in new_items:
                    new_items.append(num)
                    flag[num] = 1

    print(between_nums)
    print(new_items)
    print(flag)


if __name__ == '__main__':
    a = [2,6]
    b = [24,36]
    getTotalX(a,b)
