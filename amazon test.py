#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fillMissingBrackets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def check_balanced(s):
    # start = ["[", "("]
    # stop = [")", "]"]
    # question_count = 0
    # start_square = 0
    # end_square = 0
    # start_paran = 0
    # end_paran = 0
    start_square = s.count("[")
    end_square = s.count("]")
    start_paran = s.count("(")
    end_paran = s.count(")")
    question_count = s.count("?")
    if start_square == end_square and start_paran == end_paran:
        return True
    elif abs(start_square - end_square) + abs(start_paran - end_paran) == question_count:
        return True
    return False


def fillMissingBrackets(s):
    # Write your code here
    count = 0
    for idx, character in enumerate(s):
        if idx == len(s) -1 :
            break
        sub_str1 = s[0:idx + 1]
        sub_str2 = s[idx + 1:]
        if check_balanced(sub_str1) and check_balanced(sub_str2):
            count += 1

    return count


if __name__ == '__main__':
    print(fillMissingBrackets("[[[[]??[][[[][][[]][]][[[?]]]]?[][[][]]][]][[]]][?[]][[[[[]]]]][][][[]]]]]][]]]][[[]]]][]]][[]]][?][][?[[[[[][[]][]][][[[[?[[][[?][[[]][[[][][[?[[]]?]]]]]]][[[]][]?[["))