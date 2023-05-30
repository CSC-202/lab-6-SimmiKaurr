class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Stack:
    stack = Stack()
    return stack
    raise NotImplementedError("Stack.initialize() not defined")


def isEmpty(data: Stack) -> bool:
    if not data:
        return True
    else:
        return False
    raise NotImplementedError("Stack.isEmpty() not defined")


def push(data: Stack, value: int) -> Stack:
    if not data:
        return True
    elif len(data) == 1 and isinstance(data[0], Stack):
        return data[0].isEmpty()
    else:
        return False
    raise NotImplementedError("Stack.push() not defined")


def pop(data: Stack) -> tuple[Node, Stack]:
    if data.isEmpty():
        raise ValueError("Stack is empty.")
        
    popped_node = data.top
    data.top = data.top.next
    popped_node.next = None

    return popped_node, data
    raise NotImplementedError("Stack.pop() not defined")


def peek(data: Stack) -> Node:
    if data.isEmpty():
        raise ValueError("Stack is empty.")
        
    return data.top
    raise NotImplementedError("Stack.peek() not defined")


def clear(data: Stack) -> Stack:
    if data.isEmpty():
            return data
        
    data.top = None

    return data.clear()

    raise NotImplementedError("Stack.clear() not defined")
