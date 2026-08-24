class Node:
    def __init__(self, key=0, value=0):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
            self.map[key] = node

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            lru.prev.next = self.tail
            self.tail.prev = lru.prev
            del self.map[lru.key]

        
