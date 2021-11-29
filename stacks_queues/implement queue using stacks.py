class MyQueue:

    def __init__(self):
        self.start = []

    def push(self, x: int) -> None:
        self.start.append(x)

    def pop(self) -> int:
        return self.start.pop(0)

    def peek(self) -> int:
        return self.start[0]

    def empty(self) -> bool:
        if len(self.start)>0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_4)