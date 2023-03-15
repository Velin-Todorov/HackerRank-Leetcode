class MyQueue:

    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        x = self.items[::-1]
        element = x.pop()
        self.items = x[::-1]

        return element

    def peek(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        if not self.items:
            return True
        return False
