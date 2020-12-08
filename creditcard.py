# Enter your code here. Read input from STDIN. Print output to STDOUT

def ReverseDigits(num):
    #convert integer to a list of digits and reverse
    num_list = [int(k) for k in str(num)]
    num_list.reverse()
    #turn list back into integer 
    s = [str(m) for m in num_list] 
    return int("".join(s)) 
    
def SumOddDigits(num):
    odd_total = 0
    #convert integer to a list of digits 
    num_list = [int(k) for k in str(num)]
    for j in range(0,len(num_list),2):
        odd_total += num_list[j]
    return odd_total
        
def EvenDigits(num):
    even_digits = []
    #convert integer to a list of digits 
    num_list = [int(k) for k in str(num)]
    for t in range(1,len(num_list),2):
        even_digits.append(2*num_list[t])
    for n in range(len(even_digits)):
        if even_digits[n] > 9:
            #convert integer to a list of digits and sum
            value = [int(v) for v in str(even_digits[n])]
            even_digits[n] = sum(value)
        even_digits.append(even_digits[n])
    return sum(even_digits)

def CheckSumTest(CreditCards):
    for i in range(len(CreditCards)):
        test_num = ReverseDigits(CreditCards[i])
        A = SumOddDigits(test_num)
        B = EvenDigits(test_num)
        if (A+B)%10 == 0:
            print("Yes")
        else:
            print("No")

def main():
    data = [5,1094738249371849,7654839207594875]
    CheckSumTest(data)
main()