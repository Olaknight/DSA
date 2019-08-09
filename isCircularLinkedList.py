class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def isLooped(myList):
    p = myList.next
    q = myList.next.next

    while p is not q:
        try:
            p = p.next
            q = q.next.next
        except:
            return False

    if p is q:
        return True
    return False



myList = Node(1)
myList.next = Node(2)
myList.next.next = Node(3)
myList.next.next.next = Node(4)
myList.next.next.next.next = None


print(isLooped(myList))