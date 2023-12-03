class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not isinstance(node, Node):
            node = Node(data=node)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def delete(self):
        if not self.head:
            print("Empty list")
        if not self.head.next:
            self.head = None
        else:
            next_node = self.head.next
            while next_node.next.next:
                next_node = next_node.next
            self.tail = next_node
            next_node.next = None
    
    def insert(self, index, added_node):
        if not self.head:
            print('Empty list')
            return
        if not isinstance(added_node, Node):
            added_node = Node(data=added_node)
        if index == 0:
            added_node.next = self.head
            self.head = added_node
            return
        current_index = 0
        node = self.head
        while current_index != index-1:
            node = node.next
            current_index += 1
            if not node:
                print('Length of list is not long enough')
                return
        next_node = node.next
        node.next = added_node
        added_node.next = next_node
    
    def reverse(self):
        previous = None
        current = self.head
        self.tail = current
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

linkedlist = LinkedList()
linkedlist.append(node1)
linkedlist.append(node2)
linkedlist.append(node3)
linkedlist.append(node4)
# linkedlist.append(node5)
print(linkedlist.reorderList().data)

# node = linkedlist.head
# while node:
#     print(node.data)
#     node = node.next
# print(f'Head: {linkedlist.head.data}, Tail: {linkedlist.tail.data}')
