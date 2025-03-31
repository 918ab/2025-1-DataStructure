class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head: #LinkedList가 노드가 하나도 없는 상태(비어있는 상태)
            self.head = Node(data) #새노드를 head에 연결
            return
        current = self.head
        while current.link:
            current = current.link #다음노드로 이동
        current.link = Node(data)
    def __str__(self):
        node = self.head
        out = ""
        while node is not None:
            # print(node.data)
            out = out +str(node.data) + " -> "
            node = node.link
        return out + "end"
ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)

