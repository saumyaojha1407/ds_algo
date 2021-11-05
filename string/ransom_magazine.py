"""
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}
        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1

        for i in ransomNote:
            if i not in magazine_dict:
                return False
            magazine_dict[i] -= 1
            if magazine_dict[i] == -1:
                return False
        return True


abc = Solution()

test_case = [["a", "b"], ["aa", "ab"], ["aa", "aab"]]

for case in test_case:
    print(abc.canConstruct(case[0], case[1]))