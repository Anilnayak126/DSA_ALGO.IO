class HashMap:
    def __init__(self,size):
        self.size = size
        self.arr = [None for i in range(size)]

    def get_hash(self,key):
        return sum([ord(i) for i in key]) % self.size

    def put(self,key,value):
        index = self.get_hash(key)
        self.arr[index] = value
        print(f'data added in to array at {index}')

    def get(self,key):
        index = self.get_hash(key)
        if index > len(self.arr):
            print('There is No key Like this')
            return
        data = self.arr[index]
        if data:
            print(data,"at", index)
            return
        print('there is no data like this')

    def delete(self,key):
        index = self.get_hash(key)
        data = self.arr[index]
        if data:
            self.arr[index] = None
            print(key,'--> data deleted')
            return
        print('There is No data like this')




h=HashMap(10)

h.put('top','anil')
h.get('to')
h.delete('top')
print(h.arr)


