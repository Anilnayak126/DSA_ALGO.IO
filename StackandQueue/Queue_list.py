Queue = []


def start(list):
    def enqueue(args,data):
        args.append(data)
        print(f"{data} added")
    def dequeue(args):
        if len(args) == 0:
            print("Queue is Empty..")
        del args[0]
        print('First ele deleted..')
    def display(args):
        if len(args) == 0:
            print("Queue is Empty.")
        for i in args:
            print(i)

    while True:
        print("1. PUSH")
        print('2. POP')
        print('3.DISPLAY')
        choice = input('enter ur choice :')

        if choice == '1':
            data = input("enter a data to  enqueue:")
            enqueue(list,data)
        elif choice =='2':
            dequeue(list)
        elif choice == '3':
            display(list)
        else:
            break

if  __name__ == '__main__':
    start(Queue)
