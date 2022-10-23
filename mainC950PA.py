# Hash Map

class HashMap:
    def __init__(self):# method that initializes the itself a constructor.
        self.size = 6  # what size should I make it.
        self.map = [None] * self.size # sets hashmap to empty in all slots and sets them to all indexes

    def _get_hash(self, key): # method that gets hash
        hash = 0 # idk why hash is set to 0
        for char in str(key): # for loop that calculates from key to index and returns index
            hash += ord(char)
        return hash % self.size

    def add(self, key, value): # gets cell and inserts the key and value into the cell
        key_hash = self._get_hash(key)
        key_value = [key, value] #constructing a list with the key and value we want to insert

        if self.map[key_hash] is None:#Checks if cell is empty
            self.map[key_hash] = list([key_value]) #if true insert the key and value into the new list within the index
            return True
        else:
            for pair in self.map[key_hash]: # if not empty we check to see if key exists already, if so update the value
                if pair[0] == key: #if the key doesn't exists append to list. idk what that means. If keys doesn't exist add a new key/value pair
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):#get the hash given the key locate the cell if not none iterate through the pairs within the cell and find a value that matches key and return value
        key_hash = self._get_hash(key)# no key found return none
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key): #passed in key and now find key in order to find key_hash(index)
        key_hash = self._get_hash(key)#check if key cell is none if so return false. Key value doesnt exist

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):# need index in order to remove from list
            if self.map[key_hash][i][0] == key:#when Item is found, use pop to remove the item.
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
print(h.keys())