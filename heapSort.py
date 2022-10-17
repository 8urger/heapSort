import numpy as np
from datetime import datetime
import math

def switchaRoo(A, i, largest):
    temp = A[i]
    A[i], A[largest] = A[largest], temp
    return A

def buildMaxHeap(A):
    size, heapSize = len(A), math.floor((len(A))/2)
    for i in range(heapSize, -1, -1):
        maxHeapify(A, i, size)
    return A

def maxHeapify(A, i, length):
    L, R, largest = 2*i+1, 2*i+2, i
    if (L < length and A[L] > A[i]): largest = L      
    else: largest = i
    if (R < length and A[R] > A[largest]): largest = R          
    if (largest != i):
        switchaRoo(A, i, largest)
        maxHeapify(A, largest, length)
    return A

def heapSort(A):
    buildMaxHeap(A)
    length = len(A)
    #does the call to switcharoo increase runtime?
    for i in range(len(A)-1, 0, -1):
        switchaRoo(A, 0, i)
        length -= 1
        maxHeapify(A, 0, length)
    return A

if __name__ == "__main__":
    start=datetime.now()
    testing = np.random.randint(1, 500, np.random.randint(100, 1000))
    heapSort(testing)
    print(testing)
    print("You sorted ", len(testing), " random numbers in ", datetime.now()-start, " seconds.")
    

