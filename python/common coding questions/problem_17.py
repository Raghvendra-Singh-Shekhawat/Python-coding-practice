# Find the Nth Term of the Fibonacci Series :

number = int(input("Enter the number: "))

n1, n2 = 0, 1
sum = 0

if number<= 0:
    print("enter a number greater than zero")
else:
    for i in range(number):
        n1 = n2
        n2 = sum
        sum = n1 + n2
    print(n2)