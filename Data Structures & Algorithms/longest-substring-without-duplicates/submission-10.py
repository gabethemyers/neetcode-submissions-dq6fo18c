class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        left = 0
        right = 1
        best_length = 0

        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        for i, char in enumerate(s):
            print(char)
            print(seen_chars)
            while char in seen_chars and seen_chars[char] >= left:
                left += 1
                print("left increased ", left)
            seen_chars[char] = i
            right += 1
            print("right increased ", right)
            
            best_length = max(right - left - 1, best_length) 
            print(best_length)
            print()
        
        return best_length
            

        