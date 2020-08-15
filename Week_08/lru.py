class Node:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        self.capacity = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        node = self.m[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.val = value
            self.move_to_head(node)
            return
        node = Node(key, value)
        self.insert_head(node)
        self.m[key] = node
        self.count += 1
        if self.count > self.capacity:
            tail = self.del_tail()
            self.m.pop(tail.key)
            self.count -= 1
        self.pp()
    
    def move_to_head(self, node: 'Node'):
        self.remove(node)
        self.insert_head(node)

    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.pp()

    def remove(self, node: 'None'):
        prev = node.prev
        next_node = node.next
        next_node.prev = prev
        prev.next = next_node

    def del_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node