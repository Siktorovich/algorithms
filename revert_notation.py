# 86883509

ACTIONS = '*+-/'


class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def pop(self):
        if self.size == 0:
            return 'error'
        self.size -= 1
        return self.items.pop()

    def push(self, value):
        self.items.append(value)
        self.size += 1
        return


if __name__ == '__main__':
    stack = Stack()
    revert_notation_string = input().split()
    for item in revert_notation_string:
        if item not in ACTIONS:
            stack.push(item)
        elif item == '*':
            stack.push(int(stack.pop()) * int(stack.pop()))
        elif item == '-':
            stack.push(- (int(stack.pop())) + int(stack.pop()))
        elif item == '+':
            stack.push(int(stack.pop()) + int(stack.pop()))
        elif item == '/':
            second, first = int(stack.pop()), int(stack.pop())
            stack.push(first // second)

    print(stack.pop())
