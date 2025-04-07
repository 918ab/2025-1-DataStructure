class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.head
            self.top = node
    def pop(self):
        if self.top is None:
            #raise  IndexError("스텍이 비어있습니다")
            return "Stack is Empty"
        poped_node = self.top
        self.top = self.top.link
        return poped_node.data

s1 = Stack()
print(s1.pop())
s1.push("자료구조")
print(s1.pop())
