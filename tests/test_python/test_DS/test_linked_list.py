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
def test_initialize_with_float_value():
    node = Node(3.14)
    assert node.value == 3.14
    assert node.next is None

def test_initialize_with_next_node_object():
    next_node = Node(2.71)
    node = Node(3.14, next_node)
    assert node.value == 3.14
    assert node.next == next_node

def test_initialize_with_non_float_value():
    with pytest.raises(TypeError):
        node = Node("Hello")
        assert node.value == "Hello"
        assert node.next is None

def test_node_next_type():
    with pytest.raises(TypeError):
        node = Node(10.5)
        node.next = "invalid"


# test linked_list
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

    assert linked_list_sample.to_list() == [1, 2, 3, 5, 4]

def test_insert_head(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.insert(to_append_node, 0)

    assert linked_list_sample.to_list() == [5, 1, 2, 3, 4]
    assert linked_list_sample.head == to_append_node

def test_insert_end(linked_list_sample):
    to_append_node = Node(5)

    linked_list_sample.insert(to_append_node, 4)

    assert linked_list_sample.to_list() == [1, 2, 3, 4, 5]
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

def test_delete(linked_list_sample):
    linked_list_sample.delete(2)

    assert  linked_list_sample.to_list() == [1, 2, 4]

def test_delete_head(linked_list_sample):
    linked_list_sample.delete(0)

    assert  linked_list_sample.to_list() == [2, 3, 4]

def test_delete_end(linked_list_sample):
    linked_list_sample.delete(3)

    assert linked_list_sample.to_list() == [1, 2, 3]
    
def test_delete_empty(linked_list_empty):
    with pytest.raises(IndexError):
        linked_list_empty.delete(1)

def test_delete_out_range(linked_list_sample):
    with pytest.raises(IndexError):
        linked_list_sample.delete(4)

def test_reverse(linked_list_sample):
    linked_list_sample.reverse()

    assert linked_list_sample.to_list() == [4, 3, 2, 1]

def test_reverse_empty(linked_list_empty):
    linked_list_empty.reverse()

    assert not linked_list_empty.to_list()

def test_reverse_one(linked_list_one):
    linked_list_one.reverse()

    assert linked_list_one.to_list() == [1]

def test_reverse_two(linked_list_two):
    linked_list_two.reverse()

    assert linked_list_two.to_list() == [2, 1]






  