from TST.node import Node

class TernarySearchTree(object):
    def __init__(self):
        self.root = None

    def put(self,key,val):    
        self.root = self.putItem(self.root,key,val,0)
        print("inserted")

    def putItem(self,node,key,val,index):
        
        c = key[index]

        if node == None :
            node = Node(c)

        if  c < node.char :
            node.left = self.putItem(node.left , key , val , index)
        elif c > node.char :
            node.right = self.putItem(node.right , key ,val , index)
        elif index < len(key)-1 :
            node.mid = self.putItem( node.mid , key ,val , index+1 )
        else :
            node.val = val
        return node                  

    def get(self , key ):
        print(self.getItem(self.root,key,0))

    def getItem(self,node,key,index):
        if node == None:
            return None
        else:
            c = key[index]
            
            if index < len(key)-1 :
                return self.getItem(node.mid,key,index+1)
            elif c < node.char :
                return self.getItem(node.left,key,index)
            elif c > node.char :
                return self.getItem(node.right,key,index)
            else:
                return node.val            





                 

