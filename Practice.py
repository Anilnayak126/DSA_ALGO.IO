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
        temp = self.front
        while temp.next:
            temp = temp.next
        self.rear.next = new_node
        self.rear = new_node
    def pop(self):
        if self.front is None:
            print("Queue is Empty..")
            return
        temp = self.front
        self.front = temp.next
        temp.next = None

    def display(self):
        if self.front is None:
            print('Queue is Empty..')
            return
        temp = self.front
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")



q = Queue()
q.append(23)
q.append(45)
q.append(27)

q.pop()
q.display()