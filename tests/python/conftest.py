import pytest
from python.DS.linked_list import Node, Linked_List

@pytest.fixture
def linked_list_sample() -> Linked_List:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    linked_list = Linked_List(head=node1)

    return linked_list

@pytest.fixture
def linked_list_empty():
    return Linked_List()

@pytest.fixture
def linked_list_one() -> Linked_List:
    node1 = Node(1)
    linked_list = Linked_List(head=node1)

    return linked_list

@pytest.fixture
def linked_list_two() -> Linked_List:
    node1 = Node(1)
    node2 = Node(2)

    node1.next = node2
    linked_list = Linked_List(head=node1)

    return linked_list