class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        total = 0
        curr_Max = 0
        curr_Min = 0
        global_Max = nums[0]
        global_Min = nums[0]

        for i in range(len(nums)):
            total += nums[i]
            curr_Max += nums[i]
            if curr_Max > global_Max:
                global_Max = curr_Max
            if curr_Max < 0:
                curr_Max = 0

            curr_Min += nums[i]
            if curr_Min < global_Min:
                global_Min = curr_Min
            if curr_Min > 0:
                curr_Min = 0
        
        if global_Max < 0:
            return global_Max
        
        wrapped_sum = total - global_Min
        if wrapped_sum > global_Max:
            return wrapped_sum
        else:
            return global_Max
