class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = Node(data)

    def print_all(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

    def get_node(self, index):
        count = 0
        node = self.head
        while count < index:
            count += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next