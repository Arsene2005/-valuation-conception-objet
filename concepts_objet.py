
class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStack:
    def __init__(self, max_size):
        self.stack = [None] * max_size
        self.top = -1
        self.max_size = max_size

def is_full(self):
        return self.top == self.max_size - 1

def is_empty(self):
        return self.top == -1

def add_to_stack(self, item):
        if self.is_full():
            raise MyOutOfSizeException("The stack is full")
        self.top += 1
        self.stack[self.top] = item
def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("The stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item


if __name__ == '__main__':
 myStack = MyStack(3)
 myStack.add_to_stack('hello')
 myStack.add_to_stack('hello')
 print(myStack.is_full()) # False
 myStack.add_to_stack('hello')
 print(myStack.is_full()) # True
 myStack.add_to_stack('hello') # MyOutOfSizeException
 print(myStack.pop_from_stack()) # hello
 print(myStack.is_empty()) # False
 print(myStack.pop_from_stack()) # hello
 print(myStack.is_empty()) # False
 print(myStack.pop_from_stack()) # hello
 print(myStack.is_empty()) # True
 print(myStack.pop_from_stack()) #
MyEmptyStackException
