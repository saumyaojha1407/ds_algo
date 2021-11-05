class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global_max = 0
        start_index = 0
        dict_items = {}
        if not s:
            return 0
        for idx, i in enumerate(s):
            if i not in dict_items:
                dict_items[i] = idx
            else:
                if dict_items[i] + 1 >= start_index:
                    start_index = dict_items[i] + 1
                dict_items[i] = idx
            end_index = idx
            local_max = end_index - start_index
            if local_max >= global_max:
                global_max = local_max
        return global_max + 1


obj = Solution()
print(obj.lengthOfLongestSubstring('aabaab!bb'))