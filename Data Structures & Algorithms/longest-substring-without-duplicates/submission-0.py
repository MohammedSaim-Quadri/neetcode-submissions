class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            curr_char = s[right]

            if curr_char in hash_map and hash_map[curr_char]>=left:
                left = hash_map[curr_char] + 1

            hash_map[curr_char] = right

            window_size = right - left + 1
            if window_size > max_length:
                max_length = window_size

        return max_length