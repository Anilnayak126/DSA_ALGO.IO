class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def insert_at_the_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"{data} added Succesfully")
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{data} added Successfully")

    def search(self,target):
        if not self.head:
            print("The Linked list is empty..")
        current = self.head
        while current:
            if current.data == target:
                print('found')
                return
            else:
                current = current.next
        print("Not found")

    # def delete(self,data):
    #     if not self.head:
    #         print("The linked list is empty")
    #     Head = self.head
    #
    #     while Head.next:
    #         if Head.data == data:
    #             del Head
    #             print(f"deleted {data}")
    #             return
    #         else:
    #             Head = Head.next
    #     print("Not Found data like {data}")



    def display(self):
        if not self.head:
            print("list is empty !!")
            return
        current = self.head
        while current:
            print(f"{current.data} -->",end="")
            current = current.next
        print("None")

lk = LinkedList()

lk.insert_at_the_end(12)
lk.insert_at_the_end(13)
lk.insert_at_the_end(23)
lk.insert_at_the_end(89)
lk.insert_at_the_end(34)
# lk.delete(12)
lk.search(89)
lk.display()
