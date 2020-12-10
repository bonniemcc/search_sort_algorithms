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

def MergeSort(arr):
    if len(arr) > 1:
        #split array in half
        arr1 = arr[0:int(len(arr)/2)]
        arr2 = arr[int(len(arr)/2):len(arr)+1]

        MergeSort(arr1)
        MergeSort(arr2)

        k = l = m = 0

        #compare first elements of two sub arrays and sort
        while k < len(arr1) and l < len(arr2):
            if arr1[k] < arr2[l]:
                arr[m] = arr1[k]
                k += 1
            else:
                arr[m] = arr2[l]
                l += 1
            m += 1
        
        #add remaining elements
        while k < len(arr1):
            arr[m] = arr1[k]
            k +=1
            m +=1

        while l < len(arr2):
            arr[m] = arr2[l]
            l +=1
            m +=1
    
        return arr

    else:
        return arr
            
    

def main():
    matrix = [7,1,2,3,9,11,6,7,9]
    result = MergeSort(matrix)
    print(result)
main()