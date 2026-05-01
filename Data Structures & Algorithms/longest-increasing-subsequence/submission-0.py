class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        table = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(table[i], 1+table[j])

        return max(table)