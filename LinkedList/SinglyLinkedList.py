class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class Sinlgly_LinkedList:
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
        temp.next = new_node

    def insert_at_beginning(self,data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def length(self):
        temp= self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return  count -1


    def insert_at_position(self,data,postion):
        node_p = Node(data)
        if self.head is None:
            self.head = node_p
            return
        if postion > self.length():
            print("Get me a Valid a position")
            return
        temp = self.head
        for i in range(postion -1 ):
            temp = temp.next
        node_p.next = temp.next
        temp.next = node_p

    def delete_at_beggining(self):
        if self.head is None:
            print("There is Nothing ..")
            return
        temp = self.head
        self.head = temp.next
        temp.next = None
    def delete_at_end(self):
        if self.head is None:
            print("There  is nothing..")
            return

        temp = self.head.next
        prev = self.head

        while temp.next is not  None:
            temp = temp.next
            prev =prev.next
        prev.next = None

    def delete_at_position(self,pos):
        temp = self.head.next
        prev = self.head

        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next

    def display(self):
        if self.head is None:
            print("Linked List is Empty..")
            return
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")





sll = Sinlgly_LinkedList()
sll.insert_at_end(12)
sll.insert_at_end(45)
sll.insert_at_end(78)
sll.insert_at_beginning(79)
print(sll.length())
sll.insert_at_position(1,2)
# sll.delete_at_beggining()
# sll.delete_at_end()
sll.delete_at_position(2)

sll.display()


