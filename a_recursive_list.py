class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    return List()
    raise NotImplementedError("List.initialize() not defined")


def isEmpty(data: List) -> bool:
    if not data:
        return True
    elif isinstance(data, list):
        return all(isEmpty(element) for element in data)
    else:
        return False

    raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v:Node, index: int, value: int, i):
        if (i + 1) == index:
            new_node = (value, v.next)
            v.next = new_node
            return data
        elif i > index:
            raise IndexError("D:")
        else:
            return helper(v.next, index, i + 1, value)
        
    if data.first is None:
        data.first = Node(value, None)
        return data
    elif index < 0 or index >= len(data):
        raise IndexError("D:")
    else:
        return helper(data.first, index, value, i = 0)
    raise NotImplementedError("List.addAtIndex() not defined")




def removeAtIndex(data: Node, index: int) -> tuple[Node, List]:
    def helper(v: Node, index: int, i: int):
        if (i + 1) == index:
            target: Node = v.next
            v.next = target.next
            return target, data
        elif i > index:
            raise IndexError("D:")
        else:
            return helper(v.next, index, i + 1)
        
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError("D:")
    else:
        return helper(data.first, index, i = 0) 
    raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    if data.first is None:
        new_node = (value, None)
        data.first = new_node
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data
    raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
    def helper(v: Node, value: int):
        if v.next is None:
            new_node = Node(value, None)
            v.next = new_node
            return data
        else:
            return helper(v.next, value)
    
    if data.first is None:
        new_node = Node(value, None)
        data.first = new_node
        return data
    else:
        return helper(data.first, value)
    raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(v: Node, index: int, i: int):
        if i == index:
            return v
        elif i > index:
            raise IndexError("D:")
        else:
            return helper(v.next, index, i + 1)
        
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError("D:")
    else:
        return helper(data.first, index, i = 0)
    raise NotImplementedError("List.getElementAtIndex() not defined")


def clear(data: List) -> List:
    data.first = None
    return data
    raise NotImplementedError("List.clear() not defined")
