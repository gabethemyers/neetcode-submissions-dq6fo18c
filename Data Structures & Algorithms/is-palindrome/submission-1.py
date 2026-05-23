class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c




        return new_string == new_string[::-1]
        