class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        answer = 0
        # key: char, value: index seen
        seen_chars = {}

        for r in range(len(list(s))):
            current_char = s[r]
            if current_char in seen_chars:
                l = max(l, seen_chars[current_char] + 1)

            seen_chars[current_char] = r
                

            answer = max(answer, r-l + 1)
        
        return answer

