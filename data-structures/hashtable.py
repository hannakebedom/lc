'''
Hash Table
Array - Data structure used to store the data
Hash Function - Function used to convert the key into an array index
Collision Handling - How to handle the situation when two keys are mapped to the same index 
'''

class HashTable:
    def __init__(self):
        self.size = 6
        self.table = [ [] for i in range(self.size) ]
        print(self.table)
    
    def _get_hash(self, key):
        '''returns the index of the array where the key-value pair should be stored'''
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        '''uses the hash function to store the key-value pair in the backing array'''
        key_hash = self._get_hash(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            # if the key already exists, update the value
            if pair[0] == key:
                pair[1] = value
                return True
        
        # otherwise, the key does not exist in hash table, append the key-value pair to the bucket
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)

        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    # return the value if the key exists in the hash table
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self._get_hash(key)

        # return false if no such key exists in the hash
        if not self.table[key_hash]:
            return False
        
        # otherwise, delete the key-value pair from the hash table
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True

    def print(self):
        for item in self.table:
            if item:
                print(str(item))
    

h = HashTable()
h.add('Bob', '555-555-5555')
h.add('Ming', '777-777-7777')
h.print()
h.delete('Bob')
h.print()