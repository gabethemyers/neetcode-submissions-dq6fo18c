class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        left = 0
        best_length = 0


        for i, char in enumerate(s):
            if char in seen_chars and seen_chars[char] >= left:
                left = seen_chars[char] + 1
            seen_chars[char] = i
            
            best_length = max(i - left + 1, best_length) 
         
        
        return best_length
            

        