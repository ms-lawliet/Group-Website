class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

def shunting_yard(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    output = []
    operators = Stack()

    for token in infix:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while operators.peek() != '(':
                output.append(operators.pop())
            operators.pop()  # Discard the '(' from the stack
        else:
            while (not operators.is_empty() and
                   precedence.get(operators.peek(), 0) >= precedence.get(token, 0)):
                output.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        output.append(operators.pop())

    return output

def infix_to_postfix(infix):
    infix_tokens = list(infix)
    postfix_tokens = shunting_yard(infix_tokens)
    return postfix_tokens

def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(char):
        return char in precedence

    def greater_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    output = []
    ops_stack = Stack()

    for char in infix:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or char in "abcdefghijklmnopqrstuvwxyz" or char in "0123456789":
            output.append(char)
        elif char == '(':
            ops_stack.push(char)
        elif char == ')':
            while ops_stack.peek() != '(' and not ops_stack.is_empty():
                output.append(ops_stack.pop())
            ops_stack.pop()
        elif is_operator(char):
            while not ops_stack.is_empty() and ops_stack.peek() != '(' and greater_precedence(ops_stack.peek(), char):
                output.append(ops_stack.pop())
            ops_stack.push(char)

    while not ops_stack.is_empty():
        output.append(ops_stack.pop())

    joint = ''.join(output)
