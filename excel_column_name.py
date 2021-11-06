"""
Find Excel column name from a given column number

MS Excel columns have a pattern like A, B, C, …, Z, AA, AB, AC, …., AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.
Given a column number, find its corresponding Excel column name. The following are more examples.

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC
"""


def find_column_name(column_value):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if column_value <= 26:
        return alphabets[column_value - 1]
    out = ""
    while column_value > 0:
        q = column_value % 26
        out = alphabets[q-1] + out
        if q == 0:
            column_value = column_value //26 -1
        else:
            column_value = column_value // 26

    return out



test_case = [26, 51, 52, 80, 676, 702, 705]

for case in test_case:
    print(find_column_name(case))