class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty ..")
            return

        temp = self.head
        while temp:
            prev_data = temp.prev.data if temp.prev else "None"
            next_data = temp.next.data if temp.next else "None"
            print(f"{prev_data} <--P| {temp.data} |N--> {next_data}", end=" <--> ")
            temp = temp.next
        print("None")


# Testing the doubly linked list
dll = DoublyLinkedList()
dll.insert_at_end(12)
dll.insert_at_end(34)
dll.insert_at_end(45)
dll.insert_at_beginning(23)
dll.display()
