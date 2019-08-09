class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node    
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            temp = self.top
            self.top = self.top.next
            return temp.data

        return None

    def peek(self):
        if self.top:
            return self.top.data
        return None




#Bracket Matching Problem Application
def match_brackets(statement):
    myBrackets = Stack()
    for i in range(len(statement)):
        try:
            if statement[i] == '{' or statement[i] == '(' or statement[i] == '[':
                myBrackets.push(statement[i])
            elif statement[i] == '}':
                if myBrackets.pop() != '{':
                    return False
            elif statement[i] == ')':
                if myBrackets.pop() != '(':
                    return False
            elif statement[i] == ']':
                if myBrackets.pop() != '[':
                    return False
            else:
                continue
        except:
            return False
    if myBrackets.pop():
        return False
    else:
        return True
    


s = "[2344]({[[]]]})"

print(match_brackets(s))


