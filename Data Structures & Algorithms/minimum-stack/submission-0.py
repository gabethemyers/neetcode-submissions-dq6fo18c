class MinStack:

    def __init__(self):
        self.a = []
        self.extra_stack = []

    def push(self, val: int) -> None:
        self.a.append(val)
        
        if not self.extra_stack:
            self.extra_stack.append(val)
        else:
            self.extra_stack.append(min(val, self.extra_stack[-1]))

        
    def pop(self) -> None:
        self.a.pop()
        self.extra_stack.pop()
        

    def top(self) -> int:
        return self.a[-1]
        

    def getMin(self) -> int:
        return self.extra_stack[-1]
        
