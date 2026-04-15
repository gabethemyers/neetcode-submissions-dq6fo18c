class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        for char in s:
            if char in s_counts:
                s_counts[char] += 1
            else:
                s_counts[char] = 1
        t_counts = {}
        for char in t:
            if char in t_counts:
                t_counts[char] += 1
            else:
                t_counts[char] = 1
        
        if t_counts == s_counts:
            return True
        else:
            return False
        