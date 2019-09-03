from BTS.Node import Node

class BTS(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
 
        if(self.root == None):
            NewNode = Node(data)
            self.root = NewNode
            print('root element inserted')
        else:
            self.insertNew(data,self.root)
            print('element inserted')

    def insertNew(self,data,cur):
        if data < cur.data :
            if cur.left is None :
                NewNode = Node(data)
                cur.left = NewNode
            else:
                self.insertNew(data,cur.left)
        if data > cur.data :
            if cur.right is None:
                NewNode = Node(data)
                cur.right = NewNode
            else:    
                self.insertNew(data,cur.right)

    def inorder(self):
        self.displayInorder(self.root)

    def displayInorder(self,cur):
        if cur.left is not None:
            self.displayInorder(cur.left)
        print('element is :',cur.data)
        if cur.right is not None:
            self.displayInorder(cur.right)   


    def MinMax(self):
        if self.root.left is None :
            print('MIN is :',self.root.data)
        if self.root.right is None :
            print('MAX is :',self.root.data)
        else:
            print("MIN is :",self.findMin(self.root))
            print("MAX is :",self.findMax(self.root))

    def findMin(self,cur):
        if cur.left is not None :
            return self.findMin(cur.left)
        else:
            return(cur.data)

    def findMax(self,cur):        
        if cur.right is not None :
            return self.findMax(cur.right)
        else:
            return(cur.data)
             

    def delete(self,data):
        self.delElement(data,self.root,self.root)
    
    def delElement(self,data,cur,parentNode):

        if data == cur.data :

            if cur.right is None and  cur.left is None:
                if parentNode.right == cur:
                    parentNode.right = None
                else:
                    parentNode.left = None    
                del cur

            elif cur.right is None and cur.left is not None:
                temp = cur.left
                if(parentNode.left == cur):
                    parentNode.left = temp
                else:
                    parentNode.right = temp  
                del cur             

            elif cur.left is None and cur.right is not None:
                temp = cur.right
                if(parentNode.left == cur):
                    parentNode.left = temp
                else:
                    parentNode.right = temp  
                del cur       

            elif cur.right is not None and  cur.left is not None:
                temp = self.findMin(cur.right)
                cur.data = temp

                self.delElement(temp,cur.right,cur)

        elif data < cur.data :
            if cur.left is not None :
                self.delElement(data,cur.left,cur)

        elif data > cur.data :
            if cur.right is not None :
                self.delElement(data,cur.right,cur)        



                    