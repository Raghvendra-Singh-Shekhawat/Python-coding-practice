# Fibonacci Series upto nth term :

number = int(input("Enter the number: "))

n1, n2 = 0, 1
sum = 0

if number<=0:
    print("Please enter the number greater than 0")
else:
    for i in range(number):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
        
