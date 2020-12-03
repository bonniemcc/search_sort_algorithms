
'''Simple code to return string (YES/NO) depending on 
    whether k is found within 1D array A'''

def findNumber(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return 'YES'
    return 'NO'

A = [1,2,3,4,5]
k = 10

result = findNumber(A,k)

print(result)