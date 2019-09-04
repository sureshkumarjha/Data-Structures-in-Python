from Heap.heap import heap

hp = heap()
hp.insert(23)
hp.insert(5)
hp.insert(100)
hp.insert(2)
hp.insert(210)
hp.insert(211)
hp.display()
print(hp.currentpos)
hp.heapsort()