import pytest
from data_structure.linked_list import Node


def test_append(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.append(to_append_node)
    node = linked_list_sample.head

    count = 1
    while node.next:
        node = node.next
        count += 1

    assert node.value == 5
    assert not node.next 
    assert count == 5

def test_append_empty(linked_list_empty):
    to_append_node = Node(5)

    assert not linked_list_empty.head

    linked_list_empty.append(to_append_node)
    assert linked_list_empty.head.value == 5

def test_insert(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.insert(to_append_node, 3)

    list_nodes = []
    node = linked_list_sample.head
    while node.next:
        list_nodes.append(node.value)
        node = node.next
    list_nodes.append(node.value)
    assert list_nodes == [1, 2, 3, 5, 4]

def test_insert_head(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.insert(to_append_node, 0)

    list_nodes = []
    node = linked_list_sample.head
    while node.next:
        list_nodes.append(node.value)
        node = node.next
    list_nodes.append(node.value)
    assert list_nodes == [5, 1, 2, 3, 4]
    assert linked_list_sample.head == to_append_node

def test_insert_end(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.insert(to_append_node, 4)

    list_nodes = []
    node = linked_list_sample.head
    while node.next:
        list_nodes.append(node.value)
        node = node.next
    list_nodes.append(node.value)
    assert list_nodes == [1, 2, 3, 4, 5]
    assert not to_append_node.next

def test_insert_empty_head(linked_list_empty):
    to_append_node = Node(5)

    linked_list_empty.insert(to_append_node, 0)
    
    assert linked_list_empty.head == to_append_node

def test_insert_empty(linked_list_empty):
    with pytest.raises(IndexError):
        to_append_node = Node(5)

        linked_list_empty.insert(to_append_node, 1)

def test_insert_out_index(linked_list_sample):
    with pytest.raises(IndexError):
        to_append_node = Node(5)
        linked_list_sample.insert(to_append_node, 6)



  