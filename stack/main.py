# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self,data):
        if len(self.stack) > self.limit:
            raise IndexError("超出栈容量")
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop();
        else:
            raise IndexError("栈为空")

    def peek(self):
        if self.stack:
            return self.stack[-1];
        else:
            raise IndexError("栈为空")

    def is_Empty(self):
        if self.stack:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = Stack();
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())


