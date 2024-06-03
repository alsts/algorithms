class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):  # convert Key to Integer that fits the bounds of hashmap array
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)

        # Open addressing is used to resolve collisions,
        # Loop through hashed key until empty slot if not exist
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].value
            index += 1
            index = index % self.capacity  # Keep next available slot index in bounds -> will go back to first slot and forwards

        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            # Open addressing is used to resolve collisions,
            # Loop through hashed key until empty slot if not exist
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1

                # Double the array if size is more than 50% of capacity
                if self.size >= self.capacity // 2:
                    self.rehash()
                return

            # Key exist -> simply override value (no duplicates)
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity  # Keep next available slot index in bounds -> will go back to first slot and forwards

    def rehash(self):
        print("Rehashing")
        # Create doubled array and insert Nones
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0

        # Refill the array from old
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.value)


hashmap = HashMap()
hashmap.put("Alice", "NYC")
hashmap.put("Brad", "CHI")
hashmap.put("Mark", "NAR")

for i in range(hashmap.capacity):
    if hashmap.map[i]:
        print(i, " -> ", hashmap.map[i].key, " ", hashmap.map[i].value)
