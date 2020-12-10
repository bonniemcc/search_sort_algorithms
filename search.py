#Linear Search

#find n in arr
def LinearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i

def BinarySearch(arr,n):
    #find middle value
    m = arr[int(len(arr)/2)]
    if n > m:
        x = LinearSearch(arr[int(len(arr)/2):len(arr)+1],n)
        return len(arr[0:int(len(arr)/2)])+ x
    else:
        return LinearSearch(arr[0:int(len(arr)/2)],n)


def main():
    sorted_list = [1,2,3,5,6,6,7,12,14,15,15,20,33,67,82]
    num = 6
    print(BinarySearch(sorted_list,num))
main()