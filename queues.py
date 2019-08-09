class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#List based queue
class ListQueue:
    def __init__(self):
        self.size = 0
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return(self.items.pop())

class StackBasedQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
        self.count = 0

    def enqueue(self, data):
        self.inbound_stack.append(data)
        self.count += 1

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        self.count -= 1
        return self.outbound_stack.pop()
        
class NodeQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data):

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        temp = self.head
        if self.head is not None:
            if self.count > 1:
                self.head = self.head.next
                self.head.prev = None
                self.count -= 1
            elif self.count == 1:
                self.head = None
                self.tail= None
                self.count -= 1
            return temp.data
            
        return None

