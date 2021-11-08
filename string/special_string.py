"""
Special String Again

A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

Example
mnonopoo
output - 12

"""

def expand_middle(s, l, r):
    count = 0
    if l == r:
        count += 1
        if l > 0:
            check_char = s[l-1]
        else:
            check_char = s[l]
        l-=1
        r+=1
    else:
        check_char = s[l]
    while l >= 0 and r < len(s) and s[l] == s[r] == check_char:
        count+=1
        l-=1
        r+=1
    return count

def substring_count(s):
    count = 0
    for idx, sub in enumerate(s):
        count = count + expand_middle(s, idx, idx+1)
        count = count + expand_middle(s, idx, idx)
    print(count)

substring_count("mnonopoo")