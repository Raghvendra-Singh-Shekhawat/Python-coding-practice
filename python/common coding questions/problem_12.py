# Reverse of a number :

number = (input("Enter a number: "))

###### METHOD - 1
print(str(number[::-1]))

###### METHOD - 2

num = int(input("Enter a number: "))
rev = 0
while(num > 0):
    rev = (rev * 10) + num % 10
    num = num//10
print(f"reverse = {rev}")