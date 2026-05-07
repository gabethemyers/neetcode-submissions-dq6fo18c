class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operands = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operands:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                if token == "-":
                    stack.append(num1 - num2)
                if token == "*":
                    stack.append(num1 * num2)
                if token == "/":
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        
        return stack.pop()