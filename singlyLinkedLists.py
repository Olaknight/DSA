class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self, data):
        n = Node(data)
        self.size += 1
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.head.next = n
            self.head = n

    def find(self, data):
        current = self.tail
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def delete(self, data):
        current = self.tail
        if current.data == data:
            self.tail = current.next
            self.size -= 1
            return

        prev = current
        current = current.next
        
        while current:
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        return 

    def clearList(self):
        self.head = None
        self.tail = None

    def returnMiddle(self):
        fast = self.tail
        slow = self.tail

        while fast.next:
            fast = fast.next.next
            slow = slow.next

        if slow.data:
            print(slow.data)

    def printList(self):
        current = self.tail

        while current != None:
            print(current.data, '-->', end = '')
            current = current.next
        
        print("\n\n")

    def reverseList(self):
        temp = None
        cur1 = self.tail
        cur2 = self.tail.next 

        cur1.next = temp

        while cur2 != None:
            temp = cur1
            cur1 = cur2
            cur2 = cur2.next

            cur1.next = temp
        
        self.head, self.tail = self.tail, self.head 


            



        


tester = singlyLinkedList()
for i in range(1, 12):
    tester.append(i)

tester.printList()
tester.reverseList()
tester.printList()


tester.delete(1)
tester.delete(6)


tester.returnMiddle()
         
