from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class Node:
    value: float
    next: Optional['Node'] = None


class Linked_List:
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, node: Union[Node, float]):
        if not isinstance(node, Node):
            node = Node(node)

        if not self.head:
            self.head = node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = node

    def insert(self, node: Union[Node, float], index: int):
        """ insert node to a given index """
        if not isinstance(node, Node):
            node = Node(node)

        if index == 0: # if added at head
            node.next = self.head
            self.head = node
            return
        if not self.head:
            raise IndexError('index out of range')

        current_node = self.head
        for _ in range(index-1):
            if not current_node.next:
                raise IndexError('index out of range')
            current_node = current_node.next

        node.next = current_node.next
        current_node.next = node


    def delete(self, index: int):
        if not self.head:
            raise IndexError('index out of range')
        
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        for _ in range(index-1):
            if not current_node.next:
                raise IndexError('index out of range')
            current_node = current_node.next
        if not current_node.next:
            raise IndexError('index out of range')
        current_node.next = current_node.next.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def to_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return result