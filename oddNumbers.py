
'''Simple code to return and array which contains all the 
    odd intergers between (and including) the integers l and r'''

def oddNumbers(l, r):
    if l%2 == 0:
        l = l+1
    if r%2 == 0:
        r = r-1
    arr = []
    while l<=r:
        arr.append(l)
        l +=2
    return arr

L = 9
R = 10

result = oddNumbers(L,R)
print(result)