#!/usr/bin/python

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.items = []

    def push(self, x: int) -> None:
        if len(self.items) < self.maxSize:
            self.items.append(x)
        return

    def pop(self) -> int:
        return self.items.pop() if self.items else -1

    def increment(self, k: int, val: int) -> None:
        elements = None

        if k > len(self.items):
            self.items = [x + val for x in self.items]
            return

        elements = self.items[:k]
        self.items[:k] = [x + val for x in elements]

        return        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


