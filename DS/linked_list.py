from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class Node:
    value: Union[float, int]
    next: 'Node' = None

    def __setattr__(self, name, value):
        if name == 'value' and not isinstance(value, (int, float)):
            raise TypeError(f"Expected 'value' to be a float or int, but got {type(value).__name__}")
        if name == 'next' and value is not None and not isinstance(value, Node):
            raise TypeError(f"Expected 'next' to be a Node, but got {type(value).__name__}")
        super().__setattr__(name, value)

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