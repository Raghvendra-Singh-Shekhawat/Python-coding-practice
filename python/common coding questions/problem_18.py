# Factorial of a number:

number = int(input("Enter the number: "))

num = 1
if number<=0:
    print("factorial is not possible")
else:
    for i in range(1,number+1):
        num = num*i
    print(num)