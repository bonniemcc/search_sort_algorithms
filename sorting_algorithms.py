#Sorting Algorithms

import numpy as np

def BubbleSort(arr):
    for i in range(len(arr)):
        # Last i elements are already in place 
        for j in range(0, len(arr)-i-1):  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

def HeapSort(arr):
    heap = []
    while len(arr) > 0:
        #find max value and add to heap
        heap.append(max(arr))
        #remove value from array 
        arr.remove(max(arr))
    return list(reversed(heap))

        

def main():
    matrix = [7,1,2,3,9,11,7,7,9]
    result = HeapSort(matrix)
    print(result)
main()


