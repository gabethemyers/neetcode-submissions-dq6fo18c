class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren_dict = {']': '[', '}': '{', ')': '('}

        for char in s:
            if char in paren_dict:
                if not stack:
                    return False
                top = stack[-1]
                if paren_dict[char] != top:
                    return False
                
                stack.pop()
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True


        