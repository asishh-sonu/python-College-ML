class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

# A. Push five elements onto the stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# B. Pop two elements from the stack
try:
    popped_element1 = stack.pop()
    popped_element2 = stack.pop()
    print("Popped elements:", popped_element1, popped_element2)
except IndexError as e:
    print(e)

# C. Check if the stack is empty
is_stack_empty = stack.is_empty()
print("Is the stack empty?", is_stack_empty)
