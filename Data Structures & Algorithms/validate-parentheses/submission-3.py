class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        parentheses_dict = {"{": "}", "[": "]", "(": ")"}

        for c in s:
            if c in parentheses_dict:
                my_stack.append(c)
            else:
                if not my_stack:
                    return False
                if parentheses_dict[my_stack.pop()] != c:
                    return False
            

        return not my_stack



        