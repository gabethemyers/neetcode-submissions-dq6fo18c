class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        parentheses_dict = {"{": "}", "[": "]", "(": ")"}

        for c in s:
            if c in parentheses_dict:
                my_stack.append(c)
            else:
                if len(my_stack) < 1:
                    return False
                if parentheses_dict[my_stack.pop()] != c:
                    return False
            

        if len(my_stack) > 0:
            return False
        else:
            return True



        