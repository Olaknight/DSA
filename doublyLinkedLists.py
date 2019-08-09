class Node(object):
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)

        if self.head = None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
        
    def delete(self, data):
        current = self.head
        if current is None:
            return

        while current != None:
            if current.data == data:
                if current.prev = None:
                    self.head = current.next
                    self.head.prev = None

                elif current.next != None:
                    temp1 = current.prev
                    temp2 = current.next
                    temp1.next = temp2
                    temp2.prev = temp1

                else:
                    current.prev.next = None
                    self.tail = current
                
                count -= 1
                break

            else:
                current = current.next
        return