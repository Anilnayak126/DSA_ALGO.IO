
stack = list()

def start(list):
    def push(arg,data):
        if len(arg) == 0:
            arg.append(data)
            print(f"{data} added")
        elif len(arg) > 0:
            arg.insert(0,data)
            print(f"{data} added")
        else:
            pass
    def pop(arg):
        if len(arg) == 0:
            print("List is Empty..")
        del(arg[0])
        print('first element deleted')

    def display(args):
        if len(args) == 0:
            print('Stack is Empty')
        for i in args:
            print(i)

    while True:
        print("1.PUSH \n")
        print("2. POP \n")
        print("3. DISPLAY \n")
        choice = input('Enter your Choice :')

        if choice == '1':
            data = input('enter a ele to push :')
            push(list,data)
        elif choice == '2':
            pop(list)
        elif choice == '3':
            display(list)
        else:
            break


if __name__ == '__main__':
    start(stack)


