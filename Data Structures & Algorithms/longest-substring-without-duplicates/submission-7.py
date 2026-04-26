class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        max_length = 0

        left = 0
        for right, c in enumerate(s):
            if c in seen_chars and seen_chars[c] >= left:
                    left = seen_chars[c] + 1
            seen_chars[c] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
            

        