"""
First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count = {}
        # min_idx = 99999
        # for idx, i in enumerate(s):
        #     if i in count:
        #         count[i]['count'] += 1
        #     else:
        #         count[i] = {'index': idx, 'count': 1}
        # for key, value in count.items():
        #     if value['count'] == 1 and value['index'] < min_idx:
        #         min_idx = value['index']
        # if min_idx == 99999:
        #     return -1
        # return min_idx
        # count = {}
        # min_idx = 99999
        # for i in s:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # for idx, i in enumerate(s):
        #     if count[i] == 1:
        #         min_idx = min(min_idx, idx)
        # if min_idx == 99999:
        #     return -1
        # return min_idx
        m = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            if s.find(c) != -1 and s.find(c) == s.rfind(c):
                m = min(m, s.find(c));
        if m != len(s):
            return m;
        return -1;


abc = Solution()

test_case = [ "leetcode", "loveleetcode", "aabb"]

for case in test_case:
    print(abc.firstUniqChar(case))