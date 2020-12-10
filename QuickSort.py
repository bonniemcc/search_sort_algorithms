import numpy as np

def Split(arr,start,end):
    #use first value as pivot, p
    p = arr[start]
    #ignore first value since this is our pivot
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= p:
            high -= 1

        while low <= high and arr[low] <= p:
            low += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high

def QuickSort(arr,start,end):
    if start>=end:
        return

    p = Split(arr,start,end)
    QuickSort(arr, start, p-1)
    QuickSort(arr, p+1, end)

    return arr

def main():
    A = [2,11,6,7,13,5,9]
    print(QuickSort(A,0,len(A)-1))
main()