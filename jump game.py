class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        s_len = len(s)
        i = 0
        j = 0
        while j <= s_len and i < s_len:
            if i + minJump <= j <= min(i + maxJump, s_len -1) and str(s[j]) == '0':
                i = j
                j += 1
            else:
                j += 1
        if i == s_len - 1:
            return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.canReach("0000000000",2,5))