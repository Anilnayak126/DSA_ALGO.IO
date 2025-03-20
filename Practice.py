class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublelinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head  is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
    def insert_at_pos(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head

        for i in range(pos -1):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        temp = self.head
        while temp.next:
            temp =temp.next
        temp.prev.next = None
        temp.prev = None
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty..")
            return
        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        temp.next = None
    def delete_at_pos(self,pos):
        if self.head is None:
            print("Linked List is Empty..")
            return
        temp = self.head.next
        prev = self.head
        for i in range(pos -1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev= None




    def display(self):
        if self.head is None:
            print("Linked List is None..")
            return
        temp = self.head
        while temp:
            print(temp.data,end='-->')
            temp =temp.next
        print("None")

l = DoublelinkedList()
l.insert_at_end(12)
l.insert_at_end(45)
l.insert_at_end(56)
l.insert_at_beginning(23)
l.insert_at_pos(34,2)
# l.delete_at_end()
# l.delete_at_beginning()
# l.delete_at_pos(2)

l.display()