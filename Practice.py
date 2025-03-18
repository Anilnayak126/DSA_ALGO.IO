class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublylinkedList:
    def __init__(self):
        self.head = None


    def insert_at_the_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp= temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        if not self.head:
            print("there is no data in Linkedlist..")
            return
        temp = self.head
        while temp:
            print(temp.data,end="<-->")
            temp = temp.next
        print("None")

dll = DoublylinkedList()
dll.insert_at_the_end(12)
dll.insert_at_the_end(45)
dll.insert_at_the_end(56)
dll.display()


