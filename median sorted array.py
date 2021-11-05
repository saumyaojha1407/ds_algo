from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for idx, i in enumerate(nums):
            if target - i in nums and nums.index(target - i) !=idx:
                return [idx, nums.index(target - i)]

obj = Solution()
print(obj.twoSum([3,2,4], 6))