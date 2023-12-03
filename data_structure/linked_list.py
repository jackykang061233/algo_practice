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
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = node

    def insert(self, node: Union[Node, float], index: int):
        if not isinstance(node, Node):
            node = Node(node)

        if index == 0:
            if self.head:
                node.next = self.head
            self.head = node
            return

        last_node = self.head
        count = 0
        while last_node.next and count != index-1:
            count += 1
            last_node = last_node.next
        if count < index-1:
            raise IndexError('index out of range')
        else:
            next_node = last_node.next
            last_node.next = node
            node.next = next_node
            


