class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def append(self,data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        temp =self.front
        while temp.next:
            temp = temp.next
        self.rear.next = new_node
        self.rear = new_node

    def pop(self):
        if self.front is None:
            print("Linked is empty..")
            return
        if self.front == self.rear:
            self.front = None
            return

        temp = self.front
        self.front = self.front.next
        temp.next = None

    def print(self):
        if self.front is None:
            print("Queue is Empty.")
            return
        temp = self.front
        while temp:
            print(temp.data,end='-->')
            temp =temp.next




q = Queue()

q.append(12)
q.append(34)
q.append(89)
q.pop()
q.print()

