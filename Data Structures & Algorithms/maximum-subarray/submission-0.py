class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_Sum = nums[0]
        current_Sum = 0
        for i in range(len(nums)):
            if current_Sum < 0:
                current_Sum = 0
            current_Sum += nums[i]
            if current_Sum > max_Sum:
                max_Sum = current_Sum
        return max_Sum