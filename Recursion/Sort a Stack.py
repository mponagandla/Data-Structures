
class Stack():
    def __init__(self):
        self.top = -1
        self.stack = []

    def insert(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.top > -1:
            temp = self.stack[self.top]
            self.stack = self.stack[:self.top]
            self.top -= 1
            return temp
        else:
            return "Stack Empty"

    def top_element(self):
        if self.top >= 0:
            return self.stack[self.top]
        else:
            return None

    def print_stack(self):
        ptr = self.top
        while ptr >= 0:
            print(self.stack[ptr])
            ptr -= 1


def recursive_stack_sort(stack, order = "ASC"):
    if stack.top == 0:
        return stack
    last_ele = stack.pop()
    recursive_stack_sort(stack, order)
    insert_in_place(last_ele, stack, order)
    return stack


def insert_in_place(last_ele, stack, order):
    if order == "ASC":
        if stack.top < 0 or stack.top_element() <= last_ele:
            return stack.insert(last_ele)
    if order == "DESC":
        if stack.top < 0 or stack.top_element() >= last_ele:
            return stack.insert(last_ele)
    temp = stack.pop()
    insert_in_place(last_ele, stack, order)
    stack.insert(temp)
    return stack



stack = Stack()
stack.insert(11)
stack.insert(24)
stack.insert(5)
stack.insert(9)
stack.insert(6)
stack.insert(3)
stack.insert(4)
stack.insert(21)


print(stack.stack)
stk = recursive_stack_sort(stack)
print(stk.stack)
