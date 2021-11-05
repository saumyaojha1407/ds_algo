import re


class Solution:
    def myAtoi(self, s: str) -> int:
        flag = 0
        if len(s) > 0 and str(s).strip()[0] == '-':
            flag = 1
        out_x = ''
        for i in s.strip():
            if not out_x and (i == '0' or i == '-' or i == '+'):
                continue
            if not re.match(r'[0-9]', i):
                break
            out_x = out_x + i
        if not out_x:
            return 0
        out_x = int(out_x)
        if flag:
            out_x = -(out_x)
        if out_x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif out_x < -2 ** 31:
            return -2 ** 31
        else:
            return out_x


obj = Solution()
obj.myAtoi('       -42')