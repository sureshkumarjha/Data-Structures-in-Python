from DoublyLinkList.Node import node

class DoublyLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        if self.head is None:
            newNode = node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
             
    def display(self):
        cur = self.head
        while cur != self.tail :
            print(cur.data)
            cur = cur.next
        if cur == self.tail:
            print(cur.data)    


