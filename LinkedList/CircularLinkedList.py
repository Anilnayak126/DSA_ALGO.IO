class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        self.tail.next = new_node
        self.tail =new_node
        self.tail.next = self.head

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node


    def insert_at_position(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        temp = self.head
        for _ in range(pos -1):
            temp =temp.next
        new_node.next = temp.next
        temp.next = new_node

    def deletion_at_beginning(self):
        if self.head is None:
            print("Linked List is  Empty")
            return
        if self.head == self.tail:
            self.head = None
            return
        temp = self.head
        self.head = temp.next
        self.tail.next = self.head
        temp = None
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty..")
            return
        if self.head == self.tail:
            self.head = None
        temp= self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = self.head
        self.tail = None
        self.tail = temp

    def delete_at_the_position(self,pos):
        if self.head is None:
            print("Linked list is empty..")
            return
        if  self.head == self.tail:
            self.head = None
            return
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp = None
        if temp == self.tail:
            tail = prev

    def display(self):
        if self.head is None:
            print("Linked list is Empty..")
            return
        temp = self.head

        while temp:
            print(temp.data,end='-->')
            temp = temp.next
            if temp == self.head:
                break
        print(temp.data)

l = CircularLinkedList()
l.insert_at_end(56)
l.insert_at_end(67)
l.insert_at_beginning(34)
l.insert_at_position(1,2)
# l.deletion_at_beginning()
# l.delete_at_end()
# l.delete_at_the_position(2)

l.display()
