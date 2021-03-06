class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # i = self.hash_index(key)
        # self.buckets[i] = value

        # linked list implementation for collisions
        # increment the size
        self.size += 1
        # get the hash and get index of the key
        index = self.hash_index(key)
        # go to to the index
        currentNode = self.buckets[index]
        # If bucket is empty:
        if currentNode is None:
            # Create node, add it, return
            self.buckets[index] = HashTableEntry(key, value)
            return
        # else Iterate to the end of the linked list at provided index
        prevNode = currentNode
        while currentNode is not None:
            if currentNode.key == key:
                currentNode.value = value
            prevNode = currentNode
            currentNode = currentNode.next
            # traverses through the linked list until the end
        # insert new node to the end of the list
        prevNode.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # i = self.hash_index(key)
        # self.buckets[i] = None

        index = self.hash_index(key)
        # initial node head
        currentNode = self.buckets[index]

        # special case if head of the node is the one to delete
        if currentNode.key == key:
            self.buckets[index] = self.buckets[index].next
            return currentNode
        # if not deleting the head set var for prev node to the currentNode and the currentNode ot the next of head
        prevNode = currentNode
        currentNode = currentNode.next
        if currentNode is not None:
            if currentNode.key == key:
                prevNode.next = currentNode.next
                # currentNode = None
                self.size -= 1
                return currentNode
            else:
                prevNode = prevNode.next
                currentNode = currentNode.next
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # i = self.hash_index(key)
        # return self.buckets[i]

        # compute hash index
        index = self.hash_index(key)
        currentNode = self.buckets[index]

        while currentNode is not None:
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next

        if currentNode is None:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_bucket = self.buckets
        loadFactor = self.get_load_factor()
        if loadFactor > 0.7:
            self.buckets = [None] * new_capacity
        for entry in old_bucket:
            currentNode = entry
            while currentNode is not None:
                self.put(currentNode.key, currentNode.value)
                currentNode = currentNode.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
