# these are the operations that can be performedon Stack.?

class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items if items else []
        self.limit = limit

    def isEmpty(self):
        # returns true if the Stack is empty; false otherwise
        return len(self.items) == 0

    def push(self, item):
        # before you appending check if stack is full
        if self.full():  # true/false
            return None
        #overflowError
        self.items.append(item)

    def pop(self):
        # check if empty. if empty , you can not pop item.
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        # top element
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        # limit is 100
        return len(self.items) >= self.limit


    def search(self, target):
        # Check if the target is in the stack
        if target in self.items:
            # Distance from the top (0-based index)
            return len(self.items) - 1 - self.items.index(target)
        return -1  # Element not found
