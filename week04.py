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
    def search(self,target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다"
            else:
                current = current.link
        return f"{target}은(는) LinkedList 안에 존재하지 않습니다"
    def remove(self,target):
        if self.head.data == target:
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                return
            previous = current
            current = current.link

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(100))
print(ll.search(10))
print(ll.search(-9))
ll.remove(8)
print(ll)

