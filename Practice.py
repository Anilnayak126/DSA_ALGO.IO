class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"{data} is added")
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node
        print(f"{data} added..")

    def display(self):
        if not self.head:
            print("List is empty..")

        current  = self.head
        while current:
            print(f"{current.data} --> ",end="")
            current = current.next
        print("None")

link = LinkedList()

link.insert_at_end(12)
link.insert_at_end(23)
link.display()