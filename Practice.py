class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node.prev = temp.next
        temp.next = new_node


    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        temp.prev = new_node
        new_node.next =  temp
        self.head = new_node

    def  insert_at_position(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        for i in range(pos -1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is Empty..")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        temp.prev = None

    def delete_at_beginning(self):
        if self.head is None:
            print('Linked List is Empty ..')
            return
        temp = self.head
        self.head =temp.next
        temp.next.prev = None
        temp.next = None

    def delete_at_pos(self,pos):
        if self.head is None:
            print("Linked List is Empty..")
            return
        temp  = self.head.next
        prev = self.head
        for i in range(pos -1):
            temp= temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next.prev = prev
        temp.prev = None
        temp.next = None

    def display(self):
        if self.head is None:
            print('linked list is None')
            return
        temp = self.head
        while temp:
            print(temp.data,end='-->')
            temp = temp.next
        print('None')

l = DoublyLinkedList()
l.insert_at_end(12)
l.insert_at_end(34)
l.insert_at_beginning(39)
l.insert_at_position(23,2)
# l.delete_at_end()
# l.delete_at_beginning()
# l.delete_at_pos(2)
l.display()