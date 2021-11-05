class Solution:
    def expand_middle(self, s, l, r):
        res = ""
        resLen = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res = s[l:r + 1]
            resLen = r + 1 - l
            l -= 1
            r += 1
        return res, resLen


    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        current_res = ''
        current_len = 0
        for i in range(len(s)):
            even_res, even_len = self.expand_middle(s, i, i + 1)
            odd_res, odd_len = self.expand_middle(s, i, i)
            if even_len > odd_len:
                current_res = even_res
                current_len = even_len
            else:
                current_res = odd_res
                current_len = odd_len
            if current_len > resLen:
                res = current_res
                resLen = current_len
        return res


obj = Solution()
print(obj.longestPalindrome("abcba"))