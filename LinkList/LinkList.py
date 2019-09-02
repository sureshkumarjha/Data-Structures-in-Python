from LinkList.Node import node

class LinkList(object):

    def __init__(self):
        
        self.head = None
        self.counter = 0

    def insertBeg(self,data):
        self.counter += 1
        print('Element inserted',data)
        if self.head is None : 
            NewNode = node(data)  
            self.head = NewNode
        else:
            NewNode = node(data)
            NewNode.NextNode = self.head
            self.head = NewNode

    def display(self):
        print('ELEMENT DISPLAYED',self.counter)
        CurNode = self.head
            
        while CurNode.NextNode is not None :
            print('ELEMENT IS',CurNode.data)
            CurNode = CurNode.NextNode
        if CurNode.NextNode is None :
            print('ELEMENT IS',CurNode.data)

    def removeNode(self,data):
        self.counter -= 1
        CurNode = self.head
        previousNode = None

        while CurNode.NextNode is not None :
            if CurNode.data == data :
                break         
            previousNode = CurNode
            CurNode = CurNode.NextNode
            
        if CurNode == self.head :
             self.head = self.head.NextNode 
             del CurNode
        else:
            if CurNode.NextNode is None :
                previousNode.NextNode = None
                del CurNode
            else :
                previousNode.NextNode = CurNode.NextNode
                del CurNode    

                
            
            
            
            
