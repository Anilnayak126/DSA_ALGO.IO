class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None



    def insert_at_the_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def len(self):
        count = 0
        if self.head is None:
            return "Linked list is empty"
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self,target):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def display(self):
        if not self.head:
            print("linked list is empty ..")
        current = self.head

        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")


dll = DoublyLinkedList()

dll.insert_at_the_end(12)
dll.insert_at_the_end(34)
dll.insert_at_the_end(23)
dll.insert_at_the_end(78)
dll.insert_at_beginning(23)
dll.insert_at_beginning(5)
print(dll.search(12))
print(dll.len())
dll.display()
