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
    total = {"[": 0, "]": 0, "(": 0, ")": 0, "?": 0}
    current = {"[": 0, "]": 0, "(": 0, ")": 0, "?": 0}
    for i in s:
        total[i] += 1

    count = 0

    for idx, i in enumerate(s):
        if idx == len(s) - 1:
            break
        current[i] += 1
        balance_left = current["?"] - (abs(current["["] - current["]"]) +
                                       abs(current["("] - current[")"]))
        balance_right = (total["?"] - current["?"]) - (abs((total["["] - current["["]) -
                                                           (total["]"] - current["]"])) +
                                                       abs((total["["] - current["("]) -
                                                           (total[")"] - current[")"])))

        if balance_left >= 0 and balance_left % 2 == 0 and balance_right >= 0 and balance_right % 2 == 0:
            count += 1
    return count


if __name__ == '__main__':
    print(fillMissingBrackets("[[[[]??[][[[][][[]][]][[[?]]]]?[][[][]]][]][[]]][?[]][[[[[]]]]][][][[]]]]]][]]]][[[]]]][]]][[]]][?][][?[[[[[][[]][]][][[[[?[[][[?][[[]][[[][][[?[[]]?]]]]]]][[[]][]?[["))