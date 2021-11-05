"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i not in s_dict:
                return False
            s_dict[i] -= 1
            if s_dict[i] == -1:
                return False

        for key, value in s_dict.items():
            if value > 0:
                return False
        return True


abc = Solution()

test_case = [["anagram", "nagaram"], ["rat", "car"], ["ab", "a"]]

for case in test_case:
    print(abc.isAnagram(case[0], case[1]))