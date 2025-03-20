
# Last in Firstout

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print('Stack is Empty..')
            return
        if self.top.next is None:
            self.top = None
            return
        temp = self.top
        self.top = temp.next
        temp = None

    def  print(self):
        if self.top is None:
            print("Stack is empty..")
            return
        temp = self.top
        while temp:
            print(temp.data,end='-->')
            temp =temp.next
        print("None")

stack = Stack()
stack.push(12)
stack.push(78)
# stack.pop()
stack.print()