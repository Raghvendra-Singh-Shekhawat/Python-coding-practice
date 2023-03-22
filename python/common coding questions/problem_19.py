# Power of a number :

number = int(input("Enter the number: "))
power = int(input("Enter the power: "))

########  METHOD -- 1

print(pow(number,power))

########  METHOD -- 2

print(number**power)

########  METHOD -- 3

for i in range(1,power):
    number = number*number
print(number)