#  Sum of N natural numbers: 

N = int(input("Enter the first 'N' natural no. : "))

sum = 0
for i in range(1,N+1):
    sum = sum + i
    
print(f"sum of first {N} natural numbers is {sum}")