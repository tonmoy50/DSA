class MinStack:

    def __init__(self):
        self.stack = list()
        self.minimum = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum):
            self.minimum.append(min(self.minimum[-1], val))
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimum.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()