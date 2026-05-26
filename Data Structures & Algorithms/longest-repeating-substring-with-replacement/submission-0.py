class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k is the number of replacements
        # get frequency to find which character to replace
        if len(s) < 2:
            return 1

        left = 0
        max_len = 0
        max_freq = 0
        freq_count = {}
    
        # Let the loop control the right pointer index directly
        for right in range(len(s)):
            curr_char = s[right]
            
            if curr_char in freq_count:
                freq_count[curr_char] += 1
            else:
                freq_count[curr_char] = 1

            max_freq = max(max_freq, freq_count[curr_char])

            
            while (right-left + 1) - max_freq > k:
                freq_count[s[left]] -= 1
                left += 1
            max_len = right-left + 1

        return max_len







        return 1