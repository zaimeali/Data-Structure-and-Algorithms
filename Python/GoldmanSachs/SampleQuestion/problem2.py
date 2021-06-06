#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

# l = 3, r = 9 [3, 5, 7, 9]

def oddNumbers(l, r):
    num = []
    for i in range(l, r + 1):
        if i % 2 != 0:
            num.append(i)
    return num


if __name__ == '__main__':
    oddNumbers(3, 9)
