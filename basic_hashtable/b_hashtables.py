

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = 8
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << max) + hash) + ord(x)
    return hash & 0xFFFFFFFF


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_key = hash(key, 16)
    new_pair = Pair(key, value)
    index = new_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if key == hash_table.storage[index].key:
            print(f"thou would be over written")
        else:
            hash_table.storage[index].value = value
    else:
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    # '''
    # Fill this in.
    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
    # Should return None if the key is not found.
    # '''
    else:
        print(f"key not found")


def hash_table_retrieve(hash_table, key):


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
