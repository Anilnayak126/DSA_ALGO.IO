class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp


    def insert_at_beginning(self,data):
        new_node =Node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node

    def insert_at_position(self,data,pos):
        new_node = Node(data)
        temp = self.head

        for i in range(pos - 1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
    def delete_at_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("The Linked list is empty..")
            return
        temp = self.head.next
        prev = self.head

        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None
    def delete_at_position(self,pos):
        if self.head is None:
            print("Linked list is empty..")
        temp =  self.head.next
        before = self.head

        for i in range(pos - 1):
            temp =temp.next
            before = before.next

        before.next = temp.next
        temp.next.prev = before
        temp.prev = None
        temp.next = None

    def display(self):
        if self.head is None:
            print("There is Nothing..")
            return
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
dll.insert_at_the_end(23)
dll.insert_at_the_end(34)
dll.insert_at_the_end(78)
dll.insert_at_beginning(12)
dll.insert_at_position(45,2)
dll.delete_at_beginning()
# dll.delete_at_end()
dll.delete_at_position(2)
dll.display()