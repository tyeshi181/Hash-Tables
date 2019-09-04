

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    for x in string:
        hash = ((hash << max) + hash) + ord(x)
        result = hash & 0xFFFFFFFF
        return result % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key != key:


def hash_table_remove(hash_table, key):
    # '''
            # Fill this in.

            # If you try to remove a value that isn't there, print a warning.
            # '''

    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print(f"Warning: key: {key} does not exist")
    # Should return None if the key is not found.
    # '''
    else:
        hash_table.storage[index] = Pair(None, None)


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None and hash_table.storage.key == key:
        return hash_table.storage[index].value
    else:
        return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    percent = hash_table.capacity / self.capacity
    if percent > 0.75:
        new_capacity = self.capacity * 2
    for i in range(len(self.storage)):
        if self.storage[i] is not None:
            self.storage[i] = new_capacity[i]
    return new_capacity


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
