from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = -10000000
        global_max = -10000000
        local_start, local_end, global_start, global_end = 0, 0, 0, 0
        for i, idx in enumerate(nums):
            if nums[i] > nums[i] + local_max:
                local_max = nums[i]
                local_start, local_end = i, i
            else:
                local_max = nums[i] + local_max
                local_end = i
            if global_max < local_max:
                global_max = local_max
                global_start = local_start
                global_end = local_end
        print(nums[global_start:global_end + 1])
        return global_max


if __name__ == '__main__':
    abc = Solution()
    print(abc.maxSubArray([5,4,-1,7,8]))