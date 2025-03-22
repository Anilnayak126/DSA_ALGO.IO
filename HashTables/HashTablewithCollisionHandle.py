class Hash:
    def __init__(self,size):
        self.size = size
        self.table = [[] for  i in range (size)]

    def get_hash(self,key):
        return sum([ord(i) for i in key]) % self.size

    def insert(self,key,value):
        index = self.get_hash(key)
        if len(self.table[index]) > 0:
            print(f"collision detected.. at {index} at {self.table[index]}")
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append((key,value))

    def get(self,key):
        index = self.get_hash(key)
        for i in self.table[index]:
            if i[0] == key:
                return i[1]
        raise  KeyError(f"{key} Not Found..")

    def delete(self,key):
        index = self.get_hash(key)
        if len(self.table[index]) < 0:
            print('Table bucket is empty')
            return

        for i,kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return
        raise  KeyError(f"Key Not Found")

    def  __str__(self):
        return  "\n".join(f"{i} :{bucket} "for  i,bucket in enumerate(self.table))



hash_table = Hash(5)

hash_table.insert("grape", 20)
hash_table.insert("apple", 35)
hash_table.insert("kiwi", 30)
hash_table.insert("banana", 10)
hash_table.insert("melon", 25)

res = hash_table.get('melon')

print(hash_table)