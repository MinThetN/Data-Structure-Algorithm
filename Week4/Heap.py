'''
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the heap instantiation
'''
import time
import sys

class heap:
    def compare(x, y):  # a default compare function for min heap
        return x < y
        
    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < self.heapsize and self.cmp(self.a[l],self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r],self.a[largest]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
        
    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize-1] = x
        i = self.heapsize-1
        j = (i-1)//2
        while i > 0 and self.cmp(self.a[i],self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)//2

    def extract(self):
        x = self.a[0]
        last = self.heapsize-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)
            
    def __init__(self, items=[], cmp=compare):
        self.a = items.copy()
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()

if __name__ == "__main__":
    # Start timing
    start_time = time.process_time()
    
    # Read input from stdin
    input_line = sys.stdin.read().strip()
    rope_lengths = list(map(int, input_line.split()))
    
    # Solve rope cutting problem
    if len(rope_lengths) > 1:
        min_heap = heap(items=rope_lengths)
        total_cost = 0
        
        while not min_heap.empty() and min_heap.heapsize > 1:
            rope1 = min_heap.extract()
            rope2 = min_heap.extract()
            cost = rope1 + rope2
            total_cost += cost
            min_heap.insert(cost)
    
    # End timing and print
    end_time = time.process_time()
    print(end_time - start_time)
