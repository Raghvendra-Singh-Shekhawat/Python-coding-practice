# Sum of numbers in a given range:

N1 = int(input("Enter the first number : "))
N2 = int(input("Enter the second number : "))

sum = 0

for i in range(N1,N2+1):
    sum += i
print(f"sum is {sum}")