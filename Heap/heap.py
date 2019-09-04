class heap(object):
    def __init__(self):
        self.Heap_size = 10
        self.heap = [-1]*self.Heap_size
        self.currentpos = -1

    def insert(self,item):
        if self.heapfull():
            print("Heap is Full")
        else:
            self.currentpos += 1
            self.heap[self.currentpos] = item 
            self.fixup(self.currentpos)       

    def heapfull(self):
        if self.currentpos == self.Heap_size :
            return True
        else :
            return False    
    def fixup(self,index):
        parentIndex = int((index-1)/2)
        while parentIndex >= 0  and self.heap[parentIndex]<self.heap[index]:
            temp = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = temp
            index = parentIndex
            parentIndex = int((index-1)/2)  
    def display(self):
        print(self.heap)

    def heapsort(self):
        self.sorted = []
        while self.heap[0]!=-1:
            self.getmax(self.currentpos)
        print(self.sorted)    

    def getmax(self,index):
        result = self.heap[0]  
        self.sorted.append(result) 
        self.heap[0] = self.heap[self.currentpos]
        self.heap[self.currentpos] = -1
        self.currentpos -=1
        self.fixdown()
    def fixdown(self):
        for i in range(0,self.currentpos):
            leftchild = 2*i+1
            rightchild = 2*i+2 
            if(max(self.heap[leftchild],self.heap[rightchild])==self.heap[leftchild]):
                maxindex = leftchild 
            else:
                maxindex = rightchild 
            if maxindex !=-1 and self.heap[i] < self.heap[maxindex]:
                temp = self.heap[i]
                self.heap[i] = self.heap[maxindex]
                self.heap[maxindex] = temp
                print(self.heap)
            



