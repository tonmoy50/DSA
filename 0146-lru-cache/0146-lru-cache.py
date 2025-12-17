class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert_node(self, node):
        prev = self.mru.prev
        prev.next = node
        node.next = self.mru
        node.prev = prev
        self.mru.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.lru.next
            self.remove_node(node)
            del self.cache[node.key]
    
        
