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
    if index < 0:
        raise ValueError("Index msut be non-negative.")
    elif index == 0:
        return [value] + data
    elif index >= len(data):
        return data + [value]
    else:
        return [data[0]] + addAtIndex(data[1:], index - 1, value)
    raise NotImplementedError("List.addAtIndex() not defined")




def removeAtIndex(head: Node, index: int) -> tuple[Node, List]:
    if index < 0:
        raise ValueError("Index must be non-negative.")
    elif index == 0:
        return head.next, [head.data] if head is not None else []
    elif head is None:
        raise ValueError("Index out of bounds.")
    else:
        new_head, removed_data = removeAtIndex(head.next, index - 1)
        head.next = new_head
        return head, removed_data
    
    raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    if not data:
        return [value]
    else:
        return [value] + addToFront(data, value)
    raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
    if not data:
        return [value]
    else:
        return [data[0]] + addToBack(data[1:], value)
    raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:
    if index < 0:
        raise ValueError("Index must be non-negative.")
    elif index == 0:
        if list.head is None:
            raise ValueError("Index out of bounds.")
        return list.head
    elif list.head is None:
        raise ValueError("Index out of bounds.")
    else:
        return getElementAtIndex(list.head.next, index - 1)
    raise NotImplementedError("List.getElementAtIndex() not defined")


def clear(data: List) -> List:
    if not data:
        return []
    else:
        return clear(data[1:])
    raise NotImplementedError("List.clear() not defined")
